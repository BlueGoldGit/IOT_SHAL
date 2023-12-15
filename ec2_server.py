from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

zones = [
    {
        "name": "best_zone",
        "zname": "Zone_1"
    },
]

class Zone(Resource):
    def get(self, name):
        for zone in zones:
            if(name == zone["name"]):
                return zone, 200
        return "Zone not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("zname")
        args = parser.parse_args()

        for zone in zones:
            if(name == zone["name"]):
                return "Zone with name {} already exists".format(name), 400

        zone = {
            "name": name,
            "zname": args["zname"],
        }
        zones.append(zone)
        return zone, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("zname")
        args = parser.parse_args()

        for zone in zones:
            if(name == zone["name"]):
                zone["zname"] = args["zname"]
                return zone, 200
        
        zone = {
            "name": name,
            "zname": args["zname"],
        }
        zones.append(zone)
        return zone, 201

    def delete(self, name):
        global zones
        zones = [zone for zone in zones if zone["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(Zone, "/zone/<string:name>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='64000', debug=True)