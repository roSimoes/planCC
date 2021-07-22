CREATE TABLE IF NOT EXISTS global_land_temperatures_by_city (
    dt DATE NOT NULL,
    averagetemperature DECIMAL,
    averagetemperatureuncertainty DECIMAL,
    city VARCHAR(50),
    country VARCHAR(50),
    latitude VARCHAR(50),
    longitude VARCHAR(50)
);

