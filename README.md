# Xeneta-RatesTask
Http based API to calculate average daily rate between geographic groups of ports

Pre-Requisites
* Git
* IDE
* Ubuntu/Windows
* Python
* Conda

Run Web Server

Go to project root directory i.e. Xeneta-RatesTask and run below command in terminal
```bash
source ./start.sh
```

# API Endpoint Description

Request Parameters

* date_from
* date_to
* origin
* destination


API usage from curl
```bash
curl "http://localhost:8000/rates?date_from=2016-01-01&date_to=2016-01-01&origin=CNGGZ&destination=EETLL"

{
  "message": "Successfully retrieved resource",
  "data": [
    {
      "day": "2016-01-01",
      "average_price": 1155
    }
  ]
}
```

# Database

There is no change in database schema
