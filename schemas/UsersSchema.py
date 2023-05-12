from sqlalchemy import Column, Integer, String
from schemas import base

class UsersSchema(base):
    __tablename__ = 'users'

    address_geolocation_lat = Column(String(100))
    address_geolocation_long = Column(String(100))
    address_city = Column(String(100))
    address_street = Column(String(100))
    address_street_number = Column(Integer())
    address_zipcode = Column(String(100))
    id = Column(Integer())
    email = Column(String(100))
    username = Column(String(100), primary_key=True)
    password = Column(String(100))
    firstname = Column(String(100))
    lastname = Column(String(100))
    phone = Column(String(100))

    def __init__(
            self,
            address_geolocation_lat: str,
            address_geolocation_long: str,
            address_city: str,
            address_street: str,
            address_street_number: int,
            address_zipcode: str,
            id: int,
            email: str,
            username: str,
            password: str,
            firstname: str,
            lastname: str,
            phone: str
            ):

        self.address_geolocation_lat = address_geolocation_lat
        self.address_geolocation_long = address_geolocation_long,
        self.address_city = address_city,
        self.address_street = address_street
        self.address_street_number = address_street_number
        self.address_zipcode = address_zipcode
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone