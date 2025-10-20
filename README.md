# Proyecto Talento Tech - Curso Automatización QA - Comisión 252472

## Propósito del proyecto
Este proyecto es del curso **Automatización QA** del programa **Talento Tech**.  
Su objetivo es implementar y ejecutar pruebas automatizadas utilizando Python y Selenium para validar el funcionamiento de la página web **SauceDemo**.

El proyecto incluye pruebas automatizadas para las siguientes funcionalidades clave:
* **Inicio de sesión de usuario**: Verifica que un usuario pueda iniciar sesión correctamente.
* **Visualización del catálogo**: Comprueba que la página de productos se cargue correctamente, mostrando los elementos de la interfaz como el menú, los filtros y el carrito de compras.
* **Funcionalidad del carrito de compras**: Asegura que un usuario pueda agregar productos al carrito y que estos se reflejen tanto en el ícono del carrito como dentro de la página del mismo.

## Tecnologías utilizadas
Para la realización de este proyecto se han empleado las siguientes tecnologías y librerías:

* **Python**: Como lenguaje de programación base para la escritura de los scripts de prueba.
* **Selenium WebDriver**: Para la automatización de la interacción con el navegador web y la manipulación de los elementos de la página.
* **Pytest**: Como framework de pruebas para la estructuración, ejecución y reporte de los tests.
* **Webdriver Manager**: Para gestionar de forma automática la descarga y configuración del driver del navegador (en este caso, ChromeDriver).
* **Pytest-HTML**: Para generar reportes de resultados de las pruebas en formato HTML.

## Instrucciones de instalación de dependencias
Para poder ejecutar las pruebas de este proyecto, es necesario tener Python instalado y luego instalar las dependencias necesarias. 

Ejecutar el siguiente comando en la terminal para instalar dependencias:
```bash
pip install selenium webdriver-manager pytest pytest-html 
```

## Comando para ejecutar las pruebas y obtener un reporte detallado de los resultados
```bash
pytest -v --html=reports/$(date +%Y_%m_%d)_report.html
```