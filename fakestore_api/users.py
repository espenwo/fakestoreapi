import requests
import json
from fakestore_api.fake_store_communication import FakeStoreCommunication

class Users(FakeStoreCommunication):
    def __init__(self):
        self.sub_directory = "users"
        FakeStoreCommunication.__init__(self, sub_directory=self.sub_directory)
        

    def fix_users_schema(self) -> list:
        users_schema_list = list()
        for entry in self.get_all():
            entry["address_geolocation_lat"] = entry["address"]["geolocation"]["lat"]
            entry["address_geolocation_long"] = entry["address"]["geolocation"]["long"]
            entry["address_city"] = entry["address"]["city"]
            entry["address_street"] = entry["address"]["street"]
            entry["address_number"] = entry["address"]["number"]
            entry["address_zipcode"] = entry["address"]["zipcode"]
            del entry["address"]

            entry["firstname"] = entry["name"]["firstname"]
            entry["lastname"] = entry["name"]["lastname"]
            del entry["name"]
            users_schema_list.append(entry)
        return users_schema_list