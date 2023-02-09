# 100  Ladrillos
Plataforma donde las personas pueden comprar y vender participaciones en propiedades
 ### Requerimientos
 - Docker
 - Docker Compose
 

 ### Instalar Docker
 El primer paso es instalar la aplicación Docker de escritorio para su máquina local:
 - [Docker para Mac](https://docs.docker.com/docker-for-mac/install/)
 - [Docker para Windows](https://docs.docker.com/docker-for-windows/install/)
 - [Docker para Linux](https://docs.docker.com/engine/install/#server)

 Docker Compose es una herramienta adicional que se incluye automáticamente con las descargas de Docker para Mac y Windows. Sin embargo, si está en Linux, deberá agregarlo manualmente. Puede hacer esto ejecutando el comando sudo pip install docker-compose una vez completada la instalación de Docker.


### Instalacion.

Clonar el proyecto
```sh
git clone https://github.com/jdht1992/hundredbricks.git          
```

Para crear la imagen ejecutas los siguientes comandos
```sh
cd hundredbricks
docker-compose up --build
```

### Ejecutar proyecto.

Para ejecutar las migraciones, abrir otra terminal y entrar al contenedor y ejecutar los siguientes comandos.
```sh
docker-compose exec web bash 
python manage.py migrate
```

Para ejecutar los test se corre el comando.
```sh
pytest
```

## Rutas del proyecto
### hundredbricks

endpoint POST
```sh
localhost:8000/shop/api/v1/properties/
```
payload
```sh
{
    "status": "finished",
    "property_type": "building",
    "name": "Edificio A",
    "amount_brick": 200,
    "description": "Un edificio muy chingon"
}
```

endpoint GET
```sh
localhost:8000/shop/api/v1/properties/
```

endpoint POST
```sh
localhost:8000/shop/api/v1/property/<id_property>/price
```
payload
```sh
{
    "value": 100
}
```

endpoint POST
```sh
localhost:8000/shop/api/v1/basket/
```
payload
```sh
{
    "property": 1
}
```

endpoint GET
```sh
http://localhost:8000/shop/api/v1/checkout/customer_id/
```

endpoint POST
```sh
localhost:8000/shop/api/v1/order/
```
