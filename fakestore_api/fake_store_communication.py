import requests
import json

"""
    Parent class for all subdirectories. Subdirectories are:
        - products
        - carts
        - users
"""

class FakeStoreCommunication:
    def __init__(self, sub_directory: str) -> list:
        self.base_url = "https://fakestoreapi.com"
        self.sub_directory = sub_directory
        self.sub_directory_url = f"{self.base_url}/{self.sub_directory}"

    def get_all(self) -> list:
        
        response = requests.get(self.sub_directory_url)
        return response.json()
    
    def get_all_keys(self):

        data : list = self.get_all()
        for i in data:
            print(i.keys())
    
    def get_single_entry(self, index : int = 1) -> list:
        response = requests.get(self.sub_directory_url + f"/{index}")
        return response.json()
    
    def get_limit(self, limit : int = 1) -> list:
        response = requests.get(self.sub_directory_url + f"?limit={limit}")
        return response.json()
    
    def sort_results(self, ascending : bool = True) -> list:
        """
        ascending: False = descending
        Sort by ascending or descending, ascending is default
        """
        action : str = "asc"
        if not ascending:
            action = "desc"
        response = requests.get(self.sub_directory_url + f"?sort={action}")
        return response.json()
    
    def add_new(self, new_entry: dict) -> list:
        if new_entry is None:
            print("No entry provided, returning")
            return None
        response = requests.post(self.sub_directory_url, json=new_entry)
        return response.json()
    
    def delete(self, id: int) -> list:
        if id is None:
            print("No id provided, returning")
            return None
        
        response = requests.delete(self.sub_directory_url + f"/{id}")
        return response.json()
    
    def update(self, id : int, updated_entry: dict):
        response = requests.put(self.sub_directory_url + f"/{id}", json=updated_entry)
        return response.json()