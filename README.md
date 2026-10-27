
# Sistema de Gestión de Inventario

Proyecto académico desarrollado en Python como parte de la construcción de un portafolio profesional digital para la asignatura Sistemas Colaborativos de la Universidad Tecnológica de Panamá.

## Descripción

El Sistema de Gestión de Inventario es una aplicación de consola que permite registrar productos, consultar las existencias, actualizar cantidades y calcular el valor total del inventario.

Los datos se almacenan en una base de datos SQLite para conservar la información entre ejecuciones del programa.

## Problema que resuelve

Facilita el control básico de productos y existencias, evitando códigos duplicados y cantidades negativas. También permite consultar el valor de las unidades disponibles según el precio registrado.

## Tecnologías utilizadas

- **Python 3.13.14:** lenguaje de programación.
- **SQLite:** base de datos relacional para almacenar los productos.
- **Visual Studio Code:** entorno utilizado para escribir y ejecutar el código.
- **GitHub:** plataforma destinada a publicar y documentar el proyecto.

## Funcionalidades

- Registrar productos con código, nombre, precio y cantidad.
- Consultar los productos registrados.
- Actualizar las existencias de un producto.
- Calcular el valor de las existencias y el valor total del inventario.
- Rechazar códigos duplicados.
- Validar cantidades negativas.
- Informar cuando se intenta actualizar un producto inexistente.
- Conservar los datos en SQLite entre ejecuciones.

## Requisitos

- Python 3 instalado.
- Visual Studio Code u otro editor de código.
- Terminal o consola para ejecutar el programa.

SQLite está incluido en la biblioteca estándar de Python, por lo que no requiere una instalación adicional para este proyecto.

## Instalación y ejecución

1. Descarga o clona este repositorio.
2. Abre la carpeta del proyecto en Visual Studio Code.
3. Abre una terminal en esa carpeta.
4. Ejecuta el programa con el siguiente comando:

```bash
python main.py
```

La base de datos `inventario.db` se crea automáticamente al iniciar el programa si todavía no existe.

## Uso del sistema

Al ejecutar el programa aparece un menú con las siguientes opciones:

1. Agregar producto.
2. Consultar inventario.
3. Actualizar existencias.
4. Salir.

Selecciona la opción deseada e introduce los datos solicitados por el sistema.

## Pruebas realizadas

Durante el desarrollo se realizaron pruebas manuales para comprobar:

- El registro y la consulta de productos.
- La conservación de los datos después de cerrar y volver a abrir el programa.
- La actualización de existencias.
- El rechazo de cantidades negativas.
- La detección de códigos duplicados.
- La detección de códigos inexistentes.

## Capturas de pantalla

En esta sección se incorporarán capturas auténticas del menú, del registro de productos, de la consulta del inventario y de las validaciones realizadas.

## Estado del proyecto

Proyecto académico en desarrollo. Las funcionalidades descritas han sido probadas durante las sesiones de desarrollo; antes de publicar la versión definitiva se realizará una revisión integral del código y de la documentación.

## Autor

Bernabé Quijada Abrego

Estudiante de la Universidad Tecnológica de Panamá.
