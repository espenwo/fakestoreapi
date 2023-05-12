
import numpy as np
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class Product:
    id: int 
    title: str 
    price: float 
    description: str 
    category: str 
    rating_rate: float 
    rating_count: int

@dataclass
class Cart:
    id: int
    userId: int
    date: str
    product_id: list
    product_quantity: list

@dataclass
class User:
    address_geolocation_lat: str
    address_geolocation_long: str
    address_city: str
    address_street: str
    address_street_number: int
    address_zipcode: str
    id: int
    email: str
    username: str
    password: str
    firstname: str
    lastname: str
    phone: str


class DatasetCreation:
    def __init__(self, db):
        self.db = db

    def get_products_from_db(self) -> list:
        products_list = list()
        products = self.db.list_products()

        for product in products:
            prod_dataclass = Product(
                        id = product.id,
                        title = product.title,
                        price = product.price, 
                        description = product.description, # no need
                        category = product.category,
                        rating_rate = product.rating_rate,
                        rating_count = product.rating_count,
                    )
        
            products_list.append(prod_dataclass)

        return products_list


    def get_carts_from_db(self) -> list:
        carts_list = list()
        carts = self.db.list_carts()

        for cart in carts:
            cart_dataclass = Cart(
                id = cart.id, 
                userId = cart.userId, 
                date = cart.date, 
                product_id = cart.product_id, 
                product_quantity = cart.product_quantity
            )
            carts_list.append(cart_dataclass)
        return carts_list

    def get_users_from_db(self) -> list:
        users_list = list()
        users = self.db.list_users()

        for user in users:
            user_dataclass = User(
                address_geolocation_lat=user.address_geolocation_lat,
                address_geolocation_long=user.address_geolocation_long,
                address_city=user.address_city,
                address_street=user.address_street,
                address_street_number=user.address_street_number,
                address_zipcode=user.address_zipcode,
                id=user.id,
                email=user.email, # no need
                username=user.username, # no need
                password=user.password, # no need
                firstname=user.firstname, # no need
                lastname=user.lastname, # no need
                phone=user.phone # no need
            )
            users_list.append(user_dataclass)

        return users_list

    def get_carts_df(self):
        carts = self.get_carts_from_db()
        carts_df = pd.DataFrame(carts)
        one_hot_df = pd.get_dummies(carts_df["product_id"].apply(pd.Series).convert_dtypes(False).stack(), prefix="product_id").sum(level=0)
        # mapped_df = one_hot_df.mul(pd.DataFrame(carts_df['product_quantity'].values.tolist(), columns=one_hot_df.columns), axis=0)
        for i, row in carts_df.iterrows():
            quantities = row['product_quantity']
            one_hot_row = one_hot_df.loc[i]
            for j, quantity in enumerate(quantities):
                one_hot_df.loc[i, [col for col in one_hot_df.columns if col.endswith(str(row['product_id'][j]))]] *= quantity
        merged_df = carts_df.join(one_hot_df)
        
        del merged_df["product_quantity"]
        del merged_df["product_id"]

        return merged_df
    
    def get_products_df(self):
        products = self.get_products_from_db()
        products_df = pd.DataFrame(products)
        del products_df["description"]

        weighted_ratings = products_df["rating_rate"] * products_df["rating_count"]
        weighted_avg_rating = weighted_ratings.sum() / products_df['rating_count'].sum()

        products_df['rating_normalized'] = products_df['rating_rate'] / weighted_avg_rating

        return products_df
    
    def get_users_df(self):
        users = self.get_users_from_db()
        users_df = pd.DataFrame(users)
        # i know all of these can be used, but just thinking of gdpr here :))
        del users_df["email"]
        del users_df["username"]
        del users_df["password"]
        del users_df["firstname"] 
        del users_df["lastname"]
        del users_df["phone"]

        del users_df["address_zipcode"]
        del users_df["address_street_number"]
        
        # lets just suppose id is userid

        users_df.rename(columns = {"id": "userId"}, inplace=True)

        return users_df

    def create_dataset(self):

        """
            Ok, so here is an honest answer. I now have 3 datasets;
                products, users and carts
            
            all of these can now be used standalone, but it is quite clear that they can be combined
             by mapping between the datasets, i.e cart.product_id_n *= product.id->price, combined with rating
             and so on. But this is starting to take a while so i have just prepared each set and not
             combined them yet. 

             But to give an example of how one df can be prepared for ml at this point:

        """
        carts_df = self.get_carts_df()
        x = [col for col in carts_df if col.startswith('product_id')]
        y = carts_df["userId"]
        X_train, X_test, y_train, y_test = train_test_split(carts_df[x], y,test_size=0.2, random_state=42)
        
        """
        now x_train can be fitted against y_train
        and the model can predict on x_test, and tested against y_test
        """

        
