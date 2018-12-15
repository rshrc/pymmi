import requests
import json


class MapMyIndiaPython:

    def __init__(self):
        self.response = ""
        self.geocoding_api = "http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/geo_code"
        self.reverse_geocoding_api = "http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/rev_geocode"
        self.still_map_image_api = "http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/still_image?center=28.595939499830784,77.22556114196777&zoom=18&size=800x480&ssf=1&markers=28.595939,77.225561|28.596000,77.225600> "
        self.nearby_places_api = "https://atlas.mapmyindia.com/api/places/nearby/json?"
        self.eLoc_api = "http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/place_detail"  # ?place_id=<eLoc>
        self.routiong_api = "http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/route"
        self.driving_distance_matrix_api = "http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/distance"

    def geocoding(self, addr, pin):
        parameters = {"addr": addr, "pin": pin}
        self.response = requests.get(self.geocoding_api, params=parameters)
        return self.response

    def reverse_geocoding(self, latitutde, longitude):
        parameters = {"latitude": latitutde, "longitude": longitude}
        self.response = requests.get(
            self.reverse_geocoding_api, params=parameters)
        return self.response

    def auto_suggest(self, parameters):
        pass

    def still_map_image(self):
        self.response = requests.get(self.still_map_image_api)
        return self.response

    def nearby_places(self, keywords):
        self.response = requests.get(self.nearby_places_api, params=keywords)
        return self.response

    def eLoc(self, place_id):
        parameters = {'place_id': place_id}
        self.response = requests.get(self.eLoc_api, params=parameters)
        return self.response

    def routing(self, start, destination):
        # start=28.111,77.111&destination=28.22,77.22&alternatives=true&with_advices=1
        parameters = {'start': start, 'destination': destination,
                      'alternatives': "true", 'with_advices': 1}
        # self.response = requests.get(self.eLoc_api, params=parameters)
        self.response = requests.get(
            "http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/route?start=28.111,77.111&destination=28.22,77.22&alternatives=true&with_advices=1")
        return self.response

    def driving_distance_matrix(self):
        self.response = requests.get(
            " http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/distance?center=28.54589623,77.285698%7C&pts=29,78%7C30,78%7C28,79")
        return self.response


class MapMyIndiaPythonCustomLicense:

    def __init__(self, license_key):
        self.response = ""
        self.license_key = license_key
        self.geocoding_api = "http://apis.mapmyindia.com/advancedmaps/v1/" + \
            self.license_key+"/geo_code"
        self.reverse_geocoding_api = "http://apis.mapmyindia.com/advancedmaps/v1/" + \
            self.license_key+"/rev_geocode"
        self.still_map_image_api = "http://apis.mapmyindia.com/advancedmaps/v1/"+self.license_key + \
            "/still_image?center=28.595939499830784,77.22556114196777&zoom=18&size=800x480&ssf=1&markers=28.595939,77.225561|28.596000,77.225600> "
        self.nearby_places_api = "https://atlas.mapmyindia.com/api/places/nearby/json?"
        self.eLoc_api = "http://apis.mapmyindia.com/advancedmaps/v1/" + \
            self.license_key+"/place_detail"  # ?place_id=<eLoc>
        self.routiong_api = "http://apis.mapmyindia.com/advancedmaps/v1/" + \
            self.license_key+"/route"
        self.driving_distance_matrix_api = "http://apis.mapmyindia.com/advancedmaps/v1/" + \
            self.license_key+"/distance"

    def geocoding(self, addr, pin):
        parameters = {"addr": addr, "pin": pin}
        self.response = requests.get(self.geocoding_api, params=parameters)
        return self.response

    def reverse_geocoding(self, latitutde, longitude):
        parameters = {"latitude": latitutde, "longitude": longitude}
        self.response = requests.get(
            self.reverse_geocoding_api, params=parameters)
        return self.response

    def auto_suggest(self, parameters):
        pass

    def still_map_image(self):
        self.response = requests.get(self.still_map_image_api)
        return self.response

    def nearby_places(self, keywords):
        self.response = requests.get(self.nearby_places_api, params=keywords)
        return self.response

    def eLoc(self, place_id):
        parameters = {'place_id': place_id}
        self.response = requests.get(self.eLoc_api, params=parameters)
        return self.response

    def routing(self, start, destination):
        # start=28.111,77.111&destination=28.22,77.22&alternatives=true&with_advices=1
        parameters = {'start': start, 'destination': destination,
                      'alternatives': "true", 'with_advices': 1}
        # self.response = requests.get(self.eLoc_api, params=parameters)
        self.response = requests.get(
            "http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/route?start=28.111,77.111&destination=28.22,77.22&alternatives=true&with_advices=1")
        return self.response

    def driving_distance_matrix(self):
        self.response = requests.get(
            "http://apis.mapmyindia.com/advancedmaps/v1/zmaxlrqmpxqgg9wu2z859ofcgz8zs5u5/distance?center=28.54589623,77.285698%7C&pts=29,78%7C30,78%7C28,79")
        return self.response


# testing = MapMyIndiaPython()
# print(testing.routing("28.111,77.111", "28.22, 77.22").content)
