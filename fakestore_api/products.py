import requests
import json
from fakestore_api.fake_store_communication import FakeStoreCommunication

class Products(FakeStoreCommunication):
    def __init__(self):
        self.sub_directory = "products"
        FakeStoreCommunication.__init__(self, sub_directory=self.sub_directory)

    def fix_product_schema(self) -> list:
        product_schema_list = list()
        for entry in self.get_all():
            entry["rating_rate"] = entry["rating"]["rate"] 
            entry["rating_count"] = entry["rating"]["count"]
            del entry["rating"]
            product_schema_list.append(entry)
        return product_schema_list