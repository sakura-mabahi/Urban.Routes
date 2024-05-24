# Proyecto sprint 7

## Pruebas para comprobar la funcionalidad de Urban Routes. 
Este proyecto se centra en la automatización de pruebas para la aplicación web Urban Routes, que permite a los usuarios solicitar servicios de taxi. Las pruebas se realizan utilizando Selenium y Python para simular interacciones de usuario y verificar el funcionamiento de la aplicación.

En este proyecto se escriben las pruebas automatizadas para el proceso completo de pedir un taxi en Urban Routes.

Los localizadores y métodos necesarios están definidos en la clase UrbanRoutesPage en el archivo pages.py y las pruebas en la clase TestUrbanRoutes en el archivo main.py. En el archivo helpers.py se encuentra el método que regresa el código de teléfono. Y en el archivo data.py se encuentran los datos necesarios para usar la aplicación.

## Tecnologías y Técnicas Utilizadas

- Selenium: Se utiliza para la automatización de navegadores web.
- Python: El lenguaje de programación principal para escribir las pruebas y la lógica de automatización.
- ChromeDriver: El controlador del navegador web utilizado para interactuar con Google Chrome.
- Page Object Model (POM): Se emplea una arquitectura POM para organizar los elementos de la página y las acciones del usuario.

## Proceso de automatización:

1. **Clonar el repositorio**: En Git Bash se clona el repositoro: qa-project-07-es (git clone git@github.com:username/qa-project-07-es.git)

2. **Se trabaja de forma local en PyCharm**: Se actualiza la URL del servidor en el archivo `data.py`.

3. **Instalación de paquetes esenciales**: Antes de empezar las pruebas se instalaron los paquetes: pip, pytest. Se  requiere la instalación de Python y la biblioteca Selenium.

4. **Controlador de Chrome**: Se utiliza el navegador Chrome con el controlador Chrome WebDriver. 


## Pruebas realizadas:

El proyecto incluye pruebas automatizadas que cubren las siguientes acciones:

1. **Configurar la Dirección**:
   - Se verifica la capacidad de configurar la dirección de origen y destino en la aplicación.

2. **Seleccionar la Tarifa Comfort**:
   - Se comprueba que los usuarios pueden seleccionar la tarifa "Comfort".

3. **Rellenar el Número de Teléfono**:
   - Se verifica que el número de teléfono se puede ingresar correctamente.

4. **Agregar una Tarjeta de Crédito**:
   - Se asegura que los usuarios pueden agregar una tarjeta de crédito para el pago.

5. **Escribir un Mensaje para el Controlador**:
   - Se comprueba que los usuarios pueden enviar un mensaje al conductor.
     (Se ha acortado el mensaje de 'Muéstrame el camino al museo' a 'Muéstrame el camino' ya que la longitud maxima es de 24 caracteres)

6. **Pedir una Manta y Pañuelos**:
   - Se verifica la capacidad de solicitar una manta y pañuelos.

7. **Pedir 2 Helados**:
   - Se asegura que los usuarios puedan pedir dos helados.

8. **Aparece el Modal para Buscar un Taxi**:
   - Se verifica que, al completar todas las acciones anteriores, aparece el modal para buscar un taxi.

9. **Esperar a que aparezca la información del conductor en el modal**.
   - Se verifica que aparezca la información del conductor y los detalles del viaje.