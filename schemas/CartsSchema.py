from sqlalchemy import Column, Integer, String, ARRAY
from schemas import base

class CartsSchema(base):
    __tablename__ = 'carts'

    id = Column(Integer(), primary_key=True)
    userId = Column(Integer())
    date = Column(String(100))
    product_id = Column(ARRAY(Integer))
    product_quantity = Column(ARRAY(Integer))

    def __init__(self, id: int, userId: int, date: str, product_id: list, product_quantity: list):
        self.id = id
        self.userId = userId
        self.date = date
        self.product_id = product_id
        self.product_quantity = product_quantity