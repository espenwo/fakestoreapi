from sqlalchemy import Column, Integer, String, Float, LargeBinary
from schemas import base

class ProductsSchema(base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    title = Column(String(100))
    price = Column(Float())
    description = Column(String(1000))
    category = Column(String(100))
    rating_rate = Column(Float())
    rating_count = Column(Integer())
    # image = Column(LargeBinary, nullable = True)

    def __init__(
            self, 
            id: int, 
            title: str, 
            price: float, 
            description: str, 
            category: str, 
            rating_rate: float, 
            rating_count: int,
            # image
            ):
        
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.category = category
        self.rating_rate = rating_rate
        self.rating_count = rating_count
        # self.image = image
