import requests
import json
from fakestore_api.fake_store_communication import FakeStoreCommunication

class Carts(FakeStoreCommunication):
    def __init__(self):
        self.sub_directory = "carts"
        FakeStoreCommunication.__init__(self, sub_directory=self.sub_directory)

    def date_range(self):
        """
        Carts specific api call, no need as were just fetching all data
        """
        return
    
    def get_users_cart(self):
        """
        Carts specific api call, no need as were just fetching all data
        """
        return
    
    def fix_carts_schema(self) -> list:
        product_carts_list = list()

        for entry in self.get_all():
            product_id_array = list()
            product_quantity_array = list()
            for product_entry in entry["products"]:
                product_id_array.append(product_entry["productId"])
                product_quantity_array.append(product_entry["quantity"])
            
            entry["product_id"] = product_id_array
            entry["product_quantity"] = product_quantity_array
            del entry["products"]
            
            product_carts_list.append(entry)

        return product_carts_list