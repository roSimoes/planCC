#!/bin/sh

psql -U postgres -d postgres <<EOF
\copy global_land_temperatures_by_city FROM '/GlobalLandTemperaturesByCity.csv' DELIMITER ',' CSV HEADER; 
EOF