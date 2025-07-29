# SmartHome
## Credenciales
### Google (gmail)
ucuencagrupo@gmail.com
grupo8_2025

### Developer Console de Alexa 
(https://developer.amazon.com/alexa/console/ask)

### Github
https://github.com/Grupo8-HCI/SmartHome

## Ejecución del proyecto

### Instalar dependencias

En la raíz del proyecto desarrollado, abrir una terminal y ejecutar los siguientes comandos: 
#### En Linux y macOS
```
python3 -m venv .env
source ./.env/bin/activate
pip install -r requirements.txt
```
#### En windows

```
python -m venv .env
./.env/Scripts/activate
pip install -r requirements.txt
```


### Inicializar servidor
Después de instalar las dependencias, el siguiente paso es inicializar el servidor. Para esto, es necesario estar dentro del entorno virtual que creamos previamente y ejecutar los siguientes comandos:

#### En Linux y macOS

```
python3 ./main.py
```
### En Windows
```
python ./main.py
```

### Instalar cloudflared
El proceso de instalación de cloudflared dependerá del sistema operativo. En ambos casos se requiere privilegios de administrador/superusuario

#### En macOS (asumiendo que el usuario tiene homebrew instalado):

```
brew install cloudflared
```

#### En Windows (asumiendo que el usuario tiene chocolatey):

```
choco install cloudflared
```

### Exponer servidor local
En una terminal, ejecutar el siguiente comando:
```
cloudflared tunnel --url http://localhost:5000
```

Luego, hay que buscar lo siguiente (en la salida del comando):

```
+--------------------------------------------------------------------------------------------+
|  Your quick Tunnel has been created! Visit it at (it may take                              |
|  https://employment-fetish-strengths-improvements.trycloudflare.com                        |
+--------------------------------------------------------------------------------------------+
```
Este es el túnel a nuestro servidor local.

***NOTA**: esta URL cambia cada vez que se ejecuta el comando.*

### Cambiar endpoint
Es necesario cambiar el endpoint cada vez se expone el servidor local usando herramientas como cloudflared (la que se usó en este proyecto) o ngrok.

1. Dirigirse a https://developer.amazon.com/alexa/console/ask
2. En la tabla de las Alexa Skills, seleccionar la skill “SmartHome”.- 
3. Luego, en el menú de la izquierda, seleccionar “Endpoint”.
4. Seleccionar HTTPS (en caso de que no esté seleccionado).
5. En default region” necesitamos colocar la URL generada por cloudflared seguida por la ruta “/alexa”. En este ejemplo, deberíamos colocar *https://employment-fetish-strengths-improvements.trycloudflare.com/alexa*
6. Guardamos los cambios y construimosBuild Skill. Este botón está en la sección “Intents”).
7. Para más información sobre cómo se hicieron las rutas, se puede consultar la documentación oficial: *https://developer.amazon.com/en-US/docs/alexa/alexa-skills-kit-sdk-for-python/overview.html*
