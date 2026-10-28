
from pathlib import Path
import os
import sqlite3

from flask import (
    Flask, render_template, request, redirect,
    url_for, flash
)

app = Flask(__name__)

app.secret_key = os.environ.get(
    "FLASK_SECRET_KEY",
    "clave-temporal-solo-desarrollo"
)

BASE_DATOS = Path(__file__).resolve().parent / "inventario.db"


def conectar():
    conexion = sqlite3.connect(BASE_DATOS)
    conexion.row_factory = sqlite3.Row

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            codigo TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL CHECK (precio >= 0),
            cantidad INTEGER NOT NULL CHECK (cantidad >= 0)
        )
    """)

    conexion.commit()
    return conexion


@app.route("/")
def inicio():
    conexion = conectar()

    try:
        resumen = conexion.execute("""
            SELECT
                COUNT(*) AS total_productos,
                COALESCE(SUM(cantidad), 0) AS total_unidades,
                COALESCE(SUM(precio * cantidad), 0) AS valor_total,
                COALESCE(
                    SUM(CASE WHEN cantidad <= 5 THEN 1 ELSE 0 END),
                    0
                ) AS productos_bajos
            FROM productos
        """).fetchone()

        productos = conexion.execute("""
            SELECT codigo, nombre, precio, cantidad
            FROM productos
            ORDER BY nombre
        """).fetchall()

        return render_template(
            "index.html",
            resumen=resumen,
            productos=productos
        )
    finally:
        conexion.close()


@app.route("/productos")
def productos():
    busqueda = request.args.get("q", "").strip()
    conexion = conectar()

    try:
        if busqueda:
            termino = f"%{busqueda}%"
            lista = conexion.execute("""
                SELECT codigo, nombre, precio, cantidad
                FROM productos
                WHERE codigo LIKE ? OR nombre LIKE ?
                ORDER BY nombre
            """, (termino, termino)).fetchall()
        else:
            lista = conexion.execute("""
                SELECT codigo, nombre, precio, cantidad
                FROM productos
                ORDER BY nombre
            """).fetchall()

        return render_template(
            "productos.html",
            productos=lista,
            busqueda=busqueda
        )
    finally:
        conexion.close()


@app.route("/productos/nuevo", methods=["POST"])
def nuevo_producto():
    codigo = request.form.get("codigo", "").strip()
    nombre = request.form.get("nombre", "").strip()

    try:
        precio = float(request.form.get("precio", ""))
        cantidad = int(request.form.get("cantidad", ""))
        if precio < 0 or cantidad < 0:
            raise ValueError
    except ValueError:
        flash("El precio debe ser positivo y la cantidad un entero no negativo.", "error")
        return redirect(url_for("productos"))

    if not codigo or not nombre:
        flash("El código y el nombre son obligatorios.", "error")
        return redirect(url_for("productos"))

    conexion = conectar()
    try:
        conexion.execute("""
            INSERT INTO productos (codigo, nombre, precio, cantidad)
            VALUES (?, ?, ?, ?)
        """, (codigo, nombre, precio, cantidad))
        conexion.commit()
        flash("Producto registrado correctamente.", "success")
    except sqlite3.IntegrityError:
        flash("Ese código ya existe o los datos no cumplen las reglas.", "error")
    finally:
        conexion.close()

    return redirect(url_for("productos"))


@app.route("/productos/editar/<codigo>", methods=["GET", "POST"])
def editar_producto(codigo):
    conexion = conectar()

    try:
        producto = conexion.execute("""
            SELECT codigo, nombre, precio, cantidad
            FROM productos WHERE codigo = ?
        """, (codigo,)).fetchone()

        if producto is None:
            flash("No se encontró el producto solicitado.", "error")
            return redirect(url_for("productos"))

        if request.method == "POST":
            nombre = request.form.get("nombre", "").strip()

            try:
                precio = float(request.form.get("precio", ""))
                cantidad = int(request.form.get("cantidad", ""))
                if precio < 0 or cantidad < 0:
                    raise ValueError
            except ValueError:
                flash("Introduce un precio válido y una cantidad no negativa.", "error")
                return redirect(url_for("editar_producto", codigo=codigo))

            if not nombre:
                flash("El nombre es obligatorio.", "error")
                return redirect(url_for("editar_producto", codigo=codigo))

            conexion.execute("""
                UPDATE productos
                SET nombre = ?, precio = ?, cantidad = ?
                WHERE codigo = ?
            """, (nombre, precio, cantidad, codigo))
            conexion.commit()

            flash("Producto actualizado correctamente.", "success")
            return redirect(url_for("productos"))

        return render_template("editar_producto.html", producto=producto)
    finally:
        conexion.close()


@app.route("/productos/eliminar/<codigo>", methods=["POST"])
def eliminar_producto(codigo):
    conexion = conectar()

    try:
        cursor = conexion.execute(
            "DELETE FROM productos WHERE codigo = ?", (codigo,)
        )
        conexion.commit()

        if cursor.rowcount:
            flash("Producto eliminado correctamente.", "success")
        else:
            flash("No se encontró el producto.", "error")
    finally:
        conexion.close()

    return redirect(url_for("productos"))


if __name__ == "__main__":
    app.run(debug=False)
