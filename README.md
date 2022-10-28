# Xeneta-RatesTask
Http based API (FastAPI web framework) to calculate average daily rate between geographic groups of ports

## Pre-Requisites
* IDE
* Ubuntu/Windows
* Python

## Setup Postgres
We have provided a simple Docker setup for you, which will start a
PostgreSQL instance populated with the assignment data. You don't have
to use it, but you might find it convenient. If you decide to use
something else, make sure to include instructions on how to set it up.

You can execute the provided Dockerfile by running:

```bash
docker build -t ratestask .
```

This will create a container with the name *ratestask*, which you can
start in the following way:

```bash
docker run -p 0.0.0.0:5432:5432 --name ratestask ratestask
```

You can connect to the exposed Postgres instance on the Docker host IP address,
usually *127.0.0.1* or *172.17.0.1*. It is started with the default user `postgres` and `ratestask` password.

```bash
PGPASSWORD=ratestask psql -h 127.0.0.1 -U postgres
```

alternatively, use `docker exec` if you do not have `psql` installed:

```bash
docker exec -e PGPASSWORD=ratestask -it ratestask psql -U postgres
```

Keep in mind that any data written in the Docker container will
disappear when it shuts down. The next time you run it, it will start
with a clean state.

## Setup Web Server

Go to project root directory i.e. Xeneta-RatesTask and run below command in terminal
```bash
 ./start.sh (For Ubuntu/Linux)
 
 or
 
 sh ./start.sh (For Windows)
```

Open above link to starting using API swagger
http://localhost:8000/docs

## API Endpoint Description

### Request Parameters

* date_from
* date_to
* origin
* destination

### Response

List of average rates


## API usage from curl
```bash
curl "http://localhost:8000/rates?date_from=2016-01-01&date_to=2016-01-01&origin=CNGGZ&destination=EETLL"

[
  {
    "day": "2016-01-01",
    "average_price": 1155
  }
]
```

##  Database

There is no modification being done in database schema.
