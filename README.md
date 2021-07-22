# Coding Challenge

## Installation

Download from : https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data 
the datasets and move GlobalLandTemperaturesByCity.csv to planetly/db folder.

run:

```bash
docker-compose up
```

If you are using macOs, you may encounter a error will loading the dataset to the DB,
is so please run the folLowing :

```bash
docker-compose up -d
docker exec -it app-db psql -U postgres -d postgres
```
and in postgres:

```bash
\copy global_land_temperatures_by_city FROM '/GlobalLandTemperaturesByCity.csv' DELIMITER ',' CSV HEADER;
```
##doc
* GET /temperature?<top>&<startDate>&<endDate> - get list top temperatures between the dates startDate and endDate 
  
   EX : localhost:5000/temperature?top=10&startDate=08-28-2000&endDate=08-28-2001
* POST /temperature - create a temperature
  
   EX : localhost:5000/temperature

the body :
```bash
{
	"dt" : "2020-02-02",
    "averagetemperature" : 26.02,
    "averagetemperatureuncertainty" : 0.09,
    "city" : "Peniche",
    "country" : "Portugal",
    "latitude" : 39.36,
    "longitude" : -9.38
}
```

* PUT /temperature/<entity_id> - update temperature

  EX : localhost:5000/temperature

the body :
```bash
{
	"dt" : "2020-02-02",
    "averagetemperature" : 27.00,
    "city" : "Peniche"
}
```

##Examples

questions:

Question A - GET 
localhost:5000/temperature?top=1&startDate=2000-01-01&endDate=2013-09-01

response :
```bash
{
    "json_list": [
        {
            "averagetemperature": "39.15600000000001",
            "averagetemperatureuncertainty": "0.37",
            "city": "Ahvaz",
            "country": "Iran",
            "dt": [
                "2013-07-01"
            ],
            "latitude": "31.35N",
            "longitude": "49.01E"
        }
    ]
}
```

Question B - POST  localhost:5000/temperature

with body 
```bash
{
	"dt" : "2013-06-30",
    "averagetemperature" : 19.12,
    "averagetemperatureuncertainty" : 12.09,
    "city" : "Ahvaz",
    "country" : "Iran",
    "latitude" : "31.35N",
    "longitude" : "49.01E"
}
```

Question C - PUT localhost:5000/temperature
```bash
{
	"dt" : "2013-07-01",
    "averagetemperature" : 16,52,
    "city" : "Ahvaz"
}
```


##Project overview
I have spent somewhere between 6/8 hours to make this project.

I had previous knowledge of on rest APIs from a Java college project that I did over 5 years ago.

This type of work is not what I deal with every day, these 8 hours include all the study and manufacture of the application.
I would like to have more time to do this work because it was challenging and fun but the truth is that with
work and household chores, I couldn't devote the time I wanted to do it.

##Things left undone
1.Think about and implement Unit Tests

2.Improve code Readability

3.Small Front-end

