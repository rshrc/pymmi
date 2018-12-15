import flask
from flask import request, jsonify
from mmi import MapMyIndiaPython, MapMyIndiaPythonCustomLicense

app = flask.Flask(__name__)
app.config["DEBUG"] = True

api_object = MapMyIndiaPython()

usable_apis = [
    api_object.geocoding("Delhi", "110001"),
    api_object.reverse_geocoding(41, -71),
    api_object.still_map_image(),
    api_object.nearby_places("food"),
    api_object.eLoc("D75CA2"),
    api_object.routing("28.5562,77.1000", "28.6562,77.2410"),
    api_object.driving_distance_matrix(),
]


@app.route('/', methods=['GET'])
def home():
    response = "<h1>FLASK APIs</h1>"
    return response


@app.route('/geocoding', methods=['GET'])
def geocoding():
    return jsonify(usable_apis[0].content)


@app.route('/rev_geocoding', methods=['GET'])
def rev_geocoding():
    return jsonify(usable_apis[1].content)


@app.route('/still_map', methods=['GET'])
def still_map():
    return usable_apis[2].content


@app.route('/nearby_places', methods=['GET'])
def nearby_place():
    return jsonify(usable_apis[3].content)


@app.route('/eloc', methods=['GET'])
def eloc():
    return jsonify(usable_apis[4].content)


@app.route('/route', methods=['GET'])
def routing():
    return jsonify(usable_apis[5].content)


@app.route('/driving_distance', methods=['GET'])
def driving_distance():
    return jsonify(usable_apis[6].content)


app.run()
