# Crear un modulo de OpenAcademy

## Configuraciones iniciales

<img width="622" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/518919c2-a985-4036-b581-b8e51044d343">

Lo primero seria entrar en la terminal

<img width="394" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/2c86939d-1026-4f80-826d-7f61c6b6aeeb">

Ahora nos vamos a nuestra carpeta que creamos

<img width="413" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/1cfc31b3-26f0-497b-ad0b-4b2e88960863">

En el siguiente paso creamos un scaffold para crear el modulo, para ello usamos el comando "odoo scaffold" + el nombre del modulo que queremos instalar

<img width="399" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/3912dec3-2b64-4458-8a95-61b4166eae63">

Ahora con este comando le cambiamos los permisos a la carpeta del modulo para poder modificarla

## Configuracion del modulo

   tree 
  .
  ├── Readme.md
  
  ├── addons
  
  │   └── openacademy
  
  │       ├── __init__.py
  
  │       ├── __manifest__.py
  
  │       ├── controllers
  
  │       │   ├── __init__.py
  
  │       │   └── controllers.py
  
  │       ├── demo
  
  │       │   └── demo.xml
  
  │       ├── models
  
  │       │   ├── __init__.py
  
  │       │   └── models.py
  
  │       ├── security
  
  │       │   └── ir.model.access.csv
  
  │       └── views
  
  │           ├── templates.xml
  
  │           └── views.xml
  
  └── docker-compose.yml

Arbol de la carpeta de nuestro modulo de openacademy

<img width="556" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/2697af5a-6ce8-4c6f-8c1f-79c53e66522f">

Lo primero seria ir a nuestro archivo *__manifest__.py* y cambiar el nombre de nuestro modulo, una breve descripcion de lo que hace, el nombre del autor y la version del modulo

## Crear un modelo


<img width="406" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/6279cf73-5373-4993-8fc0-ebce50d44cbc">

Dentro de nuestro archivo *models.py* Agregamos el nombre, descripcion y campos de nuestra tabla

## Crear vistas
<img width="440" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/9fb5be5f-f77f-4aa3-989c-2126ad8bb1bc">
<img width="605" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/5dbb7e86-a1bf-4b59-9e0b-db5f8db19773">

Ahora nos vamos a nuestro archivo *views.py* y descomentamos esats lineas

<img width="638" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/5e4e1652-1de3-4cb7-ba63-da59a3c4efb7">


Ahora vamos a este archivo *ir.model.access.csv* para cambiar y dar permisos de vista a nuestra tabla

<img width="252" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/dbb46eb1-8d0a-4b27-bd26-35575f053cf2">

Volvemos a nuestro archivo *__manifest__.py* y y descomentamos esta linea para que este siempre cargado

## Instalacion del modulo


<img width="396" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/ce7ddaaa-8f39-4702-832c-023427ae2177">

Una vez hecha toda la configuracion reiniciamos nuestro docker compose


<img width="482" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/1754c7fa-3ec7-4b0d-8ed9-b37b8c6f9947">


Ahora buscamos nuestro modulo y lo activamos

<img width="650" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/d340610e-ff9d-462d-b446-52793a60bebc">

y ya vemos la tabla de nuestro modulo


## Base de datos en el IDE


<img width="460" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/6451ccf4-0b0b-484f-91e4-8ee9ffe11e28">


Si no tenemos creada la base de datos la creamos desde la parte superior derecha del IDE



<img width="292" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/77fe3bd4-20a2-4d3a-aa80-466e7a44b822">

Y lo hacemos publico



<img width="323" alt="image" src="https://github.com/FranciscoFerreiraT/extra-addons/assets/92456485/e37fcc29-b6a0-4515-9bda-76f6a4935dcd">

Y listo la tabla ya fue creada en el IDE







