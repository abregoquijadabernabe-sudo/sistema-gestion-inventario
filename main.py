
import sqlite3

BASE_DATOS = "inventario.db"


def conectar():
    conexion = sqlite3.connect(BASE_DATOS)
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


def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()

    if not codigo or not nombre:
        print("Error: el código y el nombre son obligatorios.")
        return

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        if precio < 0 or cantidad < 0:
            print("Error: no se permiten valores negativos.")
            return
    except ValueError:
        print("Error: introduce valores numéricos válidos.")
        return

    conexion = conectar()
    try:
        conexion.execute(
            "INSERT INTO productos (codigo, nombre, precio, cantidad) "
            "VALUES (?, ?, ?, ?)",
            (codigo, nombre, precio, cantidad)
        )
        conexion.commit()
        print("Producto registrado correctamente.")
    except sqlite3.IntegrityError:
        print("Error: ya existe un producto con ese código.")
    finally:
        conexion.close()


def consultar_inventario():
    conexion = conectar()
    productos = conexion.execute(
        "SELECT codigo, nombre, precio, cantidad "
        "FROM productos ORDER BY nombre"
    ).fetchall()
    conexion.close()

    print("\n--- INVENTARIO ACTUAL ---")
    if not productos:
        print("El inventario está vacío.")
        return

    valor_total = 0
    for codigo, nombre, precio, cantidad in productos:
        subtotal = precio * cantidad
        valor_total += subtotal
        print(f"\nCódigo: {codigo}")
        print(f"Nombre: {nombre}")
        print(f"Precio unitario: ${precio:.2f}")
        print(f"Cantidad: {cantidad}")
        print(f"Valor en existencias: ${subtotal:.2f}")

    print(f"\nVALOR TOTAL DEL INVENTARIO: ${valor_total:.2f}")


def actualizar_existencias():
    print("\n--- ACTUALIZAR EXISTENCIAS ---")
    codigo = input("Código del producto: ").strip()

    conexion = conectar()
    producto = conexion.execute(
        "SELECT nombre, cantidad FROM productos WHERE codigo = ?",
        (codigo,)
    ).fetchone()

    if producto is None:
        print("No existe un producto con ese código.")
        conexion.close()
        return

    nombre, cantidad_actual = producto
    print(f"Producto: {nombre}")
    print(f"Cantidad actual: {cantidad_actual}")

    try:
        nueva_cantidad = int(input("Nueva cantidad: "))
        if nueva_cantidad < 0:
            print("Error: la cantidad no puede ser negativa.")
            conexion.close()
            return
    except ValueError:
        print("Error: introduce una cantidad entera válida.")
        conexion.close()
        return

    conexion.execute(
        "UPDATE productos SET cantidad = ? WHERE codigo = ?",
        (nueva_cantidad, codigo)
    )
    conexion.commit()
    conexion.close()
    print("Existencias actualizadas correctamente.")


def mostrar_menu():
    print("\n" + "=" * 42)
    print(" SISTEMA DE GESTIÓN DE INVENTARIO")
    print("=" * 42)
    print("1. Agregar producto")
    print("2. Consultar inventario")
    print("3. Actualizar existencias")
    print("4. Salir")
    print("=" * 42)


def main():
    conexion = conectar()
    conexion.close()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_inventario()
        elif opcion == "3":
            actualizar_existencias()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
