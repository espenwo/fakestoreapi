
from schemas import base
import psycopg2
from schemas.ProductsSchema import ProductsSchema
from schemas.CartsSchema import CartsSchema
from schemas.UsersSchema import UsersSchema  
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, col
from schemas import base

class FakeStoreDBHandler:
    def __init__(self, db):
        self.db = db
        self.Session = sessionmaker(self.db)

    def drop_all(self):
        base.metadata.drop_all(self.db)
        base.metadata.create_all(self.db)
    
    def list_products(self, limit: int = 20) -> list[ProductsSchema]:
        with self.Session() as s:
            return s.query(ProductsSchema).order_by(col(ProductsSchema.id).asc()).limit(limit).all()
    
    def list_products_single_id(self, id: int, limit: int = 20) -> list[ProductsSchema]:
        with self.Session() as s:
            return (
                s.query(ProductsSchema)
                .where(ProductsSchema.id == id)
                .order_by(col(ProductsSchema.id).desc())
                .limit(limit)
                .all()
            )

    def add_product_entry(self, product_entry: ProductsSchema):
        with self.Session() as s:
            s.add(product_entry)
            s.commit()
    
    def list_carts(self, limit: int = 20) -> list[CartsSchema]:
        with self.Session() as s:
            return s.query(CartsSchema).order_by(col(CartsSchema.id).asc()).limit(limit).all()

    def add_carts_entry(self, carts_entry: CartsSchema):
        with self.Session() as s:
            s.add(carts_entry)
            s.commit()

    def list_users(self, limit: int = 20) -> list[UsersSchema]:
        with self.Session() as s:
            return s.query(UsersSchema).order_by(col(UsersSchema.id).asc()).limit(limit).all()

    def add_users_entry(self, users_entry: UsersSchema):
        with self.Session() as s:
            s.add(users_entry)
            s.commit()

    def list_user_single_id(self, user_id: int, limit: int = 20) -> list[UsersSchema]:
        with Session() as s:
            return (
                s.query(UsersSchema)
                .where(UsersSchema.userId == user_id)
                .order_by(col(UsersSchema.id).desc())
                .limit(limit)
                .all()
            )
        
    