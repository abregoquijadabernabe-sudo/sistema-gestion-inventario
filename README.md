
# Sistema de Gestión de Inventario

Proyecto académico desarrollado en Python para la asignatura Sistemas Colaborativos de la Universidad Tecnológica de Panamá. Forma parte de la construcción de un portafolio profesional digital orientado al desarrollo de soluciones informáticas.

## 1. Descripción del proyecto

El Sistema de Gestión de Inventario es una aplicación que permite administrar productos y controlar sus existencias mediante una interfaz web. También se conserva una versión de consola desarrollada durante la etapa inicial del proyecto.

La aplicación web utiliza Flask para gestionar las solicitudes del navegador, HTML para estructurar las páginas, CSS para definir el diseño visual y SQLite para almacenar la información de los productos.

## 2. Problema que resuelve

El sistema facilita el control básico de productos, precios y cantidades disponibles. Permite mantener organizada la información del inventario, consultar el valor de las existencias y detectar productos que requieren reposición.

Además, incorpora validaciones para evitar códigos duplicados, precios negativos y cantidades negativas.

## 3. Objetivos

### Objetivo general

Desarrollar una aplicación de gestión de inventario que permita registrar, consultar y administrar productos mediante una interfaz web conectada a una base de datos SQLite.

### Objetivos específicos

- Registrar productos con código, nombre, precio y cantidad.
- Consultar y buscar productos por código o nombre.
- Modificar los datos y las existencias de los productos.
- Eliminar productos mediante una acción confirmada por el usuario.
- Calcular el valor de las existencias y mostrar alertas de inventario.
- Documentar el desarrollo como parte de un portafolio profesional digital.

## 4. Tecnologías utilizadas

- **Python 3.13.14:** lenguaje de programación.
- **Flask 3.1.3:** framework utilizado para desarrollar la aplicación web.
- **SQLite:** sistema de base de datos relacional.
- **HTML5:** estructura de las páginas web.
- **CSS3:** diseño y presentación de la interfaz.
- **Visual Studio Code:** entorno de desarrollo.
- **GitHub:** plataforma para alojar y documentar el código fuente.

## 5. Funcionalidades

### Panel principal

- Mostrar la cantidad de productos registrados.
- Calcular el total de unidades disponibles.
- Calcular el valor total del inventario.
- Mostrar la cantidad de productos con existencias bajas.

### Gestión de productos

- Registrar productos nuevos.
- Consultar los productos almacenados.
- Buscar productos por código o nombre.
- Editar el nombre, el precio y la cantidad de un producto.
- Eliminar productos con confirmación.
- Mostrar el estado de las existencias: disponible, existencias bajas o agotado.

### Validaciones

- Rechazar códigos duplicados.
- Impedir precios negativos.
- Impedir cantidades negativas.
- Informar cuando no se encuentran productos.
- Validar los datos introducidos en los formularios.

## 6. Estructura del proyecto

```text
Sistema Inventario/
├── app.py
├── main.py
├── README.md
├── inventario.db
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── productos.html
    └── editar_producto.html
```

**Descripción de los archivos principales:**

- `app.py`: contiene las rutas y la lógica de la aplicación web.
- `main.py`: contiene la versión de consola desarrollada inicialmente.
- `inventario.db`: base de datos SQLite utilizada para almacenar los productos.
- `templates/index.html`: página del panel principal.
- `templates/productos.html`: página para buscar, registrar y administrar productos.
- `templates/editar_producto.html`: formulario de edición.
- `static/style.css`: estilos visuales de la aplicación.

## 7. Requisitos de instalación

Para ejecutar la aplicación se necesita:

- Python 3 instalado.
- Flask instalado en el entorno de Python.
- Un navegador web actualizado.
- Visual Studio Code u otro editor de código.
- Los archivos del proyecto.

SQLite está disponible mediante la biblioteca estándar de Python y no requiere instalar un servidor de base de datos independiente.

## 8. Instalación y ejecución

### 8.1. Obtener el proyecto

Descarga o clona el repositorio y abre su carpeta en Visual Studio Code.

### 8.2. Instalar Flask

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python -m pip install flask
```

### 8.3. Ejecutar la aplicación web

En la terminal, ejecuta:

```bash
python app.py
```

Cuando Flask indique que el servidor está activo, abre el navegador y visita:

```text
http://127.0.0.1:5000
```

La dirección corresponde al servidor local de desarrollo. Para utilizar la aplicación, la terminal debe permanecer abierta mientras el servidor esté ejecutándose.

### 8.4. Ejecutar la versión de consola

La versión inicial también puede ejecutarse mediante:

```bash
python main.py
```

## 9. Base de datos

La aplicación utiliza SQLite para almacenar los productos. Cada registro contiene los siguientes campos:

| Campo | Descripción |
|---|---|
| codigo | Identificador único del producto. |
| nombre | Nombre del producto. |
| precio | Precio unitario. |
| cantidad | Número de unidades disponibles. |

La tabla establece restricciones para evitar códigos duplicados, precios negativos y cantidades negativas.

Si el archivo de la base de datos no existe, la aplicación web crea la tabla al iniciarse. Si ya existe una base de datos compatible, la aplicación puede consultar los registros almacenados en ella.

## 10. Pruebas funcionales realizadas

Durante el desarrollo se realizaron pruebas manuales en el entorno local para comprobar las siguientes operaciones:

- Visualización del panel principal y lectura de los datos de SQLite.
- Registro de un producto de prueba.
- Búsqueda por código y nombre.
- Respuesta ante una búsqueda sin resultados.
- Edición de los datos de un producto.
- Eliminación de un producto de prueba.
- Identificación de productos con existencias bajas.
- Identificación de productos agotados.
- Actualización de los indicadores del panel principal.

Estas comprobaciones corresponden a las pruebas realizadas durante el desarrollo. No constituyen todavía una certificación integral del sistema ni pruebas automatizadas.

## 11. Capturas de pantalla y evidencias

En esta sección se incorporarán capturas auténticas del funcionamiento de la aplicación:

1. Panel principal con los indicadores del inventario.
2. Tabla de productos registrados.
3. Formulario para registrar productos.
4. Formulario de edición.
5. Resultado de la búsqueda.
6. Alerta de existencias bajas.
7. Estado de un producto agotado.
8. Confirmación de las operaciones de registro, edición y eliminación, cuando corresponda.

Las imágenes se agregarán al repositorio cuando se hayan preparado y organizado.

## 12. Seguridad y limitaciones actuales

Esta versión se ha desarrollado con fines académicos y se ejecuta localmente. Antes de utilizarla en un entorno real, es necesario revisar aspectos como la configuración de seguridad de Flask, la protección de las operaciones de modificación de datos, el manejo de errores y las condiciones de despliegue.

El servidor de desarrollo de Flask no está destinado a producción. La aplicación todavía requiere una revisión integral y pruebas adicionales antes de considerarse terminada.

## 13. Estado del proyecto

**Estado: en desarrollo.**

Se ha implementado una primera interfaz web conectada a SQLite y se han probado manualmente las funciones principales de gestión de productos. Quedan pendientes la revisión integral del código, la documentación definitiva, la incorporación de evidencias gráficas y la verificación de la publicación en GitHub.

## 14. Autor

**Bernabé Quijada Abrego**

Estudiante de la Universidad Tecnológica de Panamá.

Proyecto académico de la asignatura Sistemas Colaborativos.
