

import psycopg2
import requests

from sqlalchemy import create_engine  
from sqlmodel import col

from db.populate_new_db import populate_new_db
from db.fake_store_db_handler import FakeStoreDBHandler
from db.populate_new_db import populate_new_db

from fakestore_api.products import Products
from fakestore_api.carts import Carts
from fakestore_api.users import Users

from scripts.create_dataset import DatasetCreation

import argparse

def main(args):
    db = create_engine("postgresql+psycopg2://hello:world@localhost/hello_world")
    fakestore_db = FakeStoreDBHandler(db)

    if (args.run_api):
        # just to show that the api works
        if (args.run_api == "products"):
            api_data = Products().get_all()
            for entry in api_data:
                print(entry["image"])
                with open('pic_tmp.jpg', 'wb') as handle:
                    response = requests.get(entry["image"], stream=True)
                    if not response.ok:
                        print(response)
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)
                break
        if (args.run_api == "users"):
            api_data = Users().get_all()

        if (args.run_api == "carts"):
            api_data = Carts().get_all()

        # for entry in api_data:
        #     print(entry)

    if (args.repopulate_db):
        populate_new_db(db=fakestore_db)

    if (args.run_db):
        # just to show that the database works
        if (args.run_db == "products"):
            db_data = fakestore_db.list_products(limit=30)
            # loop over each table. I.e
            for product in db_data:
                print(product.category)

        if (args.run_db == "users"):
            db_data = fakestore_db.list_users(limit=30)
            # loop over each table. I.e
            for user in db_data:
                print(user.address_city)

        if (args.run_db == "carts"):
            db_data = fakestore_db.list_carts(limit=30)
            # loop over each table. I.e
            for cart in db_data:
                print(cart.product_id)

    if (args.create_dataset):
        dataset_cls = DatasetCreation(fakestore_db)
        dataset_cls.create_dataset()


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-api", choices=["users", "products", "carts"], 
                        help="Fetch data from api")
    parser.add_argument("--repopulate-db", action="store_true", help="Run command to populate database")
    parser.add_argument("--run-db", choices=["users", "products", "carts"], 
                        help="Fetch data from db")
    parser.add_argument("--create-dataset", action="store_true")
    args = parser.parse_args()

    main(args)