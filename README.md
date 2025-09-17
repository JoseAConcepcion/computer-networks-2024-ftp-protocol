# Informe breve sobre el repositorio `computer-networks-2024-ftp-protocol`

Este proyecto es el resultado final de la asignatura "Redes de Computadoras". El objetivo principal del proyecto es implementar un cliente para el protocolo File Transfer Protocol (FTP), siguiendo la especificación RFC 959. La implementación está realizada en Python.

## ¿Qué hace el proyecto según el código?

El repositorio contiene una aplicación de consola que permite conectarse a un servidor FTP y ejecutar distintos comandos propios del protocolo. Entre las funcionalidades implementadas se encuentran:

- **Conexión y autenticación:** Permite al usuario conectarse a un servidor FTP especificando IP, puerto, usuario y contraseña.
- **Navegación y gestión de directorios:** Comandos como `PWD` (mostrar directorio actual), `CWD` (cambiar directorio), `MKD` (crear directorio), y `RMD` (eliminar directorio).
- **Listado y manejo de archivos:** Comandos como `LIST` y `NLST` para listar archivos y directorios, `SIZE` para consultar el tamaño de archivos, y `DELE` para eliminar archivos.
- **Transferencia de archivos:** Implementa subida (`STOR`, `APPE`) y descarga (`RETR`) de archivos, incluyendo soporte para modos pasivo y activo.
- **Otros comandos FTP:** Apoya comandos avanzados como `RENAME` (renombrar archivos), `TYPE` (tipo de transferencia), `SITE`, `SYST`, `HELP`, entre otros.
- **Gestión de la sesión:** Permite cerrar la sesión con `QUIT` y ejecutar comandos auxiliares como `NOOP` (sin operación).

La lógica principal reside en la clase `FTPClient`, que encapsula la conexión y ejecución de comandos FTP, gestionando tanto el socket de control como el de datos, y procesando las respuestas del servidor. La interfaz de usuario se gestiona en el archivo `consoleApp.py`, donde se solicita información al usuario y se interpretan los comandos introducidos.

## Resumen

En definitiva, este proyecto es una implementación educativa completa de un cliente FTP en Python, que cubre la mayoría de las operaciones estándar del protocolo, permitiendo al usuario interactuar con servidores FTP de manera práctica y flexible desde la línea de comandos.