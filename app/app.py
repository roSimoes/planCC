from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
db = SQLAlchemy(app)




class Temperature(db.Model):
    __tablename__ = 'global_land_temperatures_by_city'
    dt = db.Column(db.Date, primary_key=True)
    averagetemperature = db.Column(db.Numeric)
    averagetemperatureuncertainty = db.Column(db.Numeric)
    city = db.Column(db.String, primary_key=True)
    country = db.Column(db.String)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)

    def __init__(self, dt, averagetemperature, averagetemperatureuncertainty, city, country, latitude, longitude):
        self.dt = dt
        self.averagetemperature = averagetemperature
        self.averagetemperatureuncertainty = averagetemperatureuncertainty
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude


    def dump_datetime(self, value):
        """Deserialize datetime object into string form for JSON processing."""
        if value is None:
            return None
        return [value.strftime("%Y-%m-%d")]

    def dump_decimal(self, value):
        """Deserialize decimal object into string form for JSON processing."""
        if value is None:
            return None
        return str(value)


    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'dt': self.dump_datetime(self.dt),
            'averagetemperature' : self.dump_decimal(self.averagetemperature),
            'averagetemperatureuncertainty' : self.dump_decimal(self.averagetemperatureuncertainty),
            'city' : self.city,
            'country' : self.country,
            'latitude' : self.latitude,
            'longitude' : self.longitude
        }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/temperature", methods=['POST', 'PUT', 'GET'])
def temperature_route():
    if request.method == 'POST':
        content = request.json
        dt = content['dt']
        city = content['city']

        averagetemperature = content['averagetemperature']
        averagetemperatureuncertainty = content['averagetemperatureuncertainty']
        country = content['country']
        latitude = content['latitude']
        longitude = content['longitude']

        if db.session.query(Temperature).filter(Temperature.dt == dt, Temperature.city == city).count() == 0:
            data = Temperature(dt, averagetemperature, averagetemperatureuncertainty, city, country, latitude, longitude)
            db.session.add(data)
            db.session.commit()
            return Response(status=200)
        else:
            return jsonify({"message":"Record already exists"})

    elif request.method == 'PUT':
        content = request.json

        dt = content.get('dt')
        city = content.get('city')
        averagetemperature = content.get('averagetemperature')
        averagetemperatureuncertainty = content.get('averagetemperatureuncertainty')

        if db.session.query(Temperature).filter(Temperature.dt == dt, Temperature.city == city).count() == 0:
            return Response(status=404)
        else:
            t = db.session.query(Temperature).filter(Temperature.dt == dt, Temperature.city == city).first()

            if averagetemperature:
                t.averagetemperature = averagetemperature
            if averagetemperatureuncertainty:
                t.averagetemperatureuncertainty = averagetemperatureuncertainty

            db.session.commit()
            return Response(status=200)


    elif request.method == 'GET':
        top = request.args.get('top')
        start = request.args.get('startDate')
        end = request.args.get('endDate')

        if not top or not start or not end :
            return jsonify({"message":"Not all attributes are collected"})

        else :
            qryresult = db.session.query(Temperature).filter(Temperature.dt <= end, Temperature.dt >= start).filter(Temperature.averagetemperature.isnot(None)).order_by(Temperature.averagetemperature.desc()).limit(top).all()


        return jsonify(json_list=[i.serialize for i in qryresult])

