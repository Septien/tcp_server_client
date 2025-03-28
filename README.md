Ejercicio de cliente/servidor con TCP.

El servidor responde al cliente con su mismo mensaje en mayúscula.

### Ejecute el servidor
Para ejecutar el servidor, desde una consola ejecute:
```
python3 server.py
```
Esto iniciará el servidor y esperará una nueva conexión de algún cliente.

### Ejecute el cliente
Para ejecutar el cliente, desde una segunda consola ejecute:
```
python3 cliente.py
```
Esto ejecutará el cliente, el cual se conectará al servidor en
`localhost` mediante el puerto `5000`.

### Mande mensaje al servidor desde el cliente
En la consola donde ejecutó el cliente se mostrará el mensaje
```
Ingrese mensaje:
```
Escriba después de este el mensaje que
quiera enviar al servidor. Como respuesta se mostrará en la 
consola el mensaje
```
Respuesta del servidor: ...
```
seguido del 
mensaje que ingresó anteriormente.

### Desconecte el cliente
Para terminar la conexión del cliente con el servidor, ingrese
`DESCONEXION` en la consola, como se muestra a continuación:
```
Ingrese mensaje: DESCONEXION
```
Esto cerrará la conexión con el
servidor y el cliente detendrá su ejecución.

El servidor continuará ejecutándose en espera de una nueva conexión.
Si desea terminar el servido, presion `Ctrl+C`.
