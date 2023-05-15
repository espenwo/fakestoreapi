from sqlmodel import Session

from schemas.ProductsSchema import ProductsSchema
from schemas.UsersSchema import UsersSchema
from schemas.CartsSchema import CartsSchema

from fakestore_api.carts import Carts
from fakestore_api.products import Products
from fakestore_api.users import Users
import requests
import os



def populate_new_db(db):
    
    db.drop_all()

    with db.Session() as s:
        product_schema_fixed = Products().fix_product_schema()
        for entry in product_schema_fixed:
            # with open('pic_tmp.jpg', 'wb') as handle:
            #     response = requests.get(entry["image"], stream=True)
            #     if not response.ok:
            #         print(response)
            #     for block in response.iter_content(1024):
            #         if not block:
            #             break
            #         handle.write(block)
            product_db_entry = ProductsSchema(
                id = entry["id"],
                title = entry["title"],
                price = entry["price"],
                description = entry["description"],
                category = entry["category"],
                rating_rate = entry["rating_rate"],
                rating_count = entry["rating_count"],
                # image = "pic_tmp.jpg"
            )
            s.add(product_db_entry)
            # if os.path.exists("pic_tmp.jpg"):
            #     os.remove("pic_tmp.jpg")
        s.commit()

        users_schema_fixed = Users().fix_users_schema()
        for entry in users_schema_fixed:
            users_db_entry = UsersSchema(
                address_geolocation_lat = entry["address_geolocation_lat"],
                address_geolocation_long = entry["address_geolocation_long"], 
                address_city = entry["address_city"],
                address_street = entry["address_street"], 
                address_street_number = entry["address_number"],
                address_zipcode = entry["address_zipcode"],
                id = entry["id"],
                email = entry["email"],
                username = entry["username"],
                password = entry["password"],
                firstname = entry["firstname"],
                lastname = entry["lastname"],
                phone = entry["phone"]
            )
            s.add(users_db_entry)
        s.commit()

        carts_schema_fixed = Carts().fix_carts_schema()
        for entry in carts_schema_fixed:
            carts_db_entry = CartsSchema(
                id = entry["id"],
                userId = entry["userId"],
                date = entry["date"],
                product_id = entry["product_id"],
                product_quantity = entry["product_quantity"]
            )
            s.add(carts_db_entry)
        s.commit()


        print("populated!")
    