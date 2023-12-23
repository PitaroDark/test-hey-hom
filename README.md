
# Prueba Tecnica Hey Hom

Se llevo a cabo la prueba tecnica impuesta por hey home logrando el objetivo que se especulan en el documento


## Despliegue

Para desplegar el proyecto en produccion, simplemente es usar docker en cualquier servidor con distribucion linux y funcionara, esta conformado por 3 servicios, los cuales son `django-api` es la API, `django-db` es la base de datos basado en PostgreSQL y `django-pgadmin` es la parte grafica de la base de datos


Aqui esta el comando y a la vez se muestra los logs del mismo proyecto
```bash
  cd test-hey-hom
  docker compose up --build
```

En caso de no querer ver los logs y dejarlo en segundo plano, es agregar `-d` en el comando, como se muestra  

```bash
  cd test-hey-hom
  docker compose up --build -d
```
## Variables de entorno

Para ejecutar este proyecto, deberá agregar las siguientes variables de entorno a su archivo .env, sin embargo, el proyecto ya tiene el archivo, usted puede modificarlo a su gusto

### Credenciales para Django

`DJANGO_ADMIN_MAIL`

`DJANGO_ADMIN_USER`

`DJANGO_ADMIN_PASS`

### Configuraciones para Django

`DJANGO_PORT`

`DJANGO_SECRET_KEY`

`DJANGO_DEBUG`

`DJANGO_ALLOWED_HOSTS`

### Credenciales para PostgreSQL

`POSTGRES_USER`

`POSTGRES_PASSWORD`

`POSTGRES_HOST`

`POSTGRES_PORT`

`POSTGRES_DB`

### Credenciales para Pgadmin

`PGADMIN_DEFAULT_EMAIL`

`PGADMIN_DEFAULT_PASSWORD`

`PGADMIN_LISTEN_PORT`

## Documentación

Aqui el diagrama entidad-relacion para mejor entendimiento

#### Entidad relacion
![Alt text](docs/Diagrama-Entidad-Relacion.png?raw=true "ER")

Al igual la API cuenta con su propia documentacion para usarla de manera externa
#### Documentación API
![Alt text](imgs/docs-api.png?raw=true "DOCS API")


## API Reference

#### Documentacion de la API

En esta ruta, usted puede acceder a la documentacion de la API la cual es generada automaticamente y probar lo que guste, sin necesidad de instalar un software externo para peticiones

```http
  GET /docs/
```

### Clientes

#### Creacion de un cliente (User)

En esta ruta, usted puede crear n clientes para generar transacciones

```http
  POST /api/clients/
```

| Parameter | Type     | Description                 |
| :-------- | :------- | :-------------------------  |
| `name`    | `string` | **Requerido**. Su nombre    |
| `lastname`| `string` | **Requerido**. Su apellido  |
| `email`   | `string` | **Requerido**. Su correo    |

### Creditos

#### top-up

En esta ruta, usted puede colocar un movimiento para agregar un monto al credito con el id del cliente

```http
  POST /api/credits/top-up
```

| Parameter | Type     | Description                          |
| :-------- | :------- | :-------------------------           |
| `amont`   | `decimal`| **Requerido**. El monto a agregar    |
| `client`  | `integer`| **Requerido**. El id del cliente     |

#### deduct

En esta ruta, usted puede retirar un monto del credito de un cliente utlizando su id

```http
  POST /api/credits/deduct
```

| Parameter | Type     | Description                          |
| :-------- | :------- | :-------------------------           |
| `amont`   | `decimal`| **Requerido**. El monto a retirar    |
| `client`  | `integer`| **Requerido**. El id del cliente     |

#### balance

En esta ruta, usted puede ver el balance del credito de un cliente utilizando su id
```http
 GET /api/credits/balance/{id_cliente}
```



## Usos/Ejemplos

#### Create Client

Para crear un usuario, puedes utilizar este esquema

```JSON
{
    "name": "hey", 
    "lastname": "hom",
    "email": "heyhome@example.com"
}
```
#### Create top-up or Create reduct

Para crear un movimiento donde agregas un monto, puedes utilizar este esquema

```JSON
{
    "amont": 1000,
    "client": 1
}
```

## Demo

A continuacion se muestra una demostracion de su uso

Primero deberas inicializar el proyecto utilizando docker y asignando todas las variables de entorno

![Alt text](imgs/deploy-docker.png?raw=true "Deploy")

![Alt text](imgs/envs.png?raw=true "Deploy")

Despues de que el proyecto este activo, podras realizar peticiones tanto en la documentacion de la API como en algun software externo, en este caso, se utilizara `insomnia` para realizar peticiones

#### Creamos el cliente

![Alt text](imgs/create-client.png?raw=true "Client")


#### Agregamos un monto al credito

![Alt text](imgs/create-top-up.png?raw=true "Top-up")

#### Retiramos un monto al credito

![Alt text](imgs/create-deduct.png?raw=true "Deduct")

#### Obtenemos el balance

![Alt text](imgs/balance.png?raw=true "Balance")

### Base de datos terminal

Usted puede ingresar a la base datos utilizando el siguiente comando y colocando la contraseña de la base de datos, que en este caso es `postgres`, como se mira en la imagen

```bash
psql -h localhost -p 5432 --dbname=credits -U postgres
```

![Alt text](imgs/db-terminal.png?raw=true "DB-TERMINAL")

### Base de datos con pgadmin

O bien, usted tambien puede abrir el apartado grafico para ver las tablas de la base datos, ingresando al puerto de pgadmin en el archivo .env, en los valores por defecto tienes `http://127.0.0.1:5433` e ingresar las credenciales que se encuentran en el mismo .env

![Alt text](imgs/db-pgadmin-1.png?raw=true "PGADMIN-CREDENTIALS")

Deberas registrar la base de datos siguiendo los pasos

![Alt text](imgs/db-pgadmin-2.png?raw=true "PGADMIN-DB")

![Alt text](imgs/db-pgadmin-3.png?raw=true "PGADMIN-DB")

![Alt text](imgs/db-pgadmin-4.png?raw=true "PGADMIN-DB")

![Alt text](imgs/db-pgadmin-5.png?raw=true "PGADMIN-DB")

### Web Admin Django

Y finalmente, puedes ingresar al apartado de admin con django utilizando como usuario `admin` y contraseña `admin`, para ingresar como se muestra en la imagen

![Alt text](imgs/django-admin.png?raw=true "ADMIN-DJANGO")
## Authors

- [@Ikari Vargas](https://www.github.com/PitaroDark)

