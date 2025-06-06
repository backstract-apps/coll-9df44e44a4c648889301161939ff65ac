from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Products(BaseModel):
    id: Any
    name: str
    description: str
    price: float
    category_id: int


class ReadProducts(BaseModel):
    id: Any
    name: str
    description: str
    price: float
    category_id: int
    class Config:
        from_attributes = True


class Categories(BaseModel):
    id: Any
    name: str


class ReadCategories(BaseModel):
    id: Any
    name: str
    class Config:
        from_attributes = True


class Customers(BaseModel):
    id: Any
    name: str
    address: str
    contact_details: str


class ReadCustomers(BaseModel):
    id: Any
    name: str
    address: str
    contact_details: str
    class Config:
        from_attributes = True


class Orders(BaseModel):
    id: Any
    order_date: Any
    customer_id: int
    total_amount: float


class ReadOrders(BaseModel):
    id: Any
    order_date: Any
    customer_id: int
    total_amount: float
    class Config:
        from_attributes = True


class OrderItems(BaseModel):
    id: Any
    order_id: int
    product_id: int
    quantity: int


class ReadOrderItems(BaseModel):
    id: Any
    order_id: int
    product_id: int
    quantity: int
    class Config:
        from_attributes = True


class Profile(BaseModel):
    id: int
    name: str
    email: str
    phone_no: int
    address: str


class ReadProfile(BaseModel):
    id: int
    name: str
    email: str
    phone_no: int
    address: str
    class Config:
        from_attributes = True




class PostProducts(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    price: str = Field(..., max_length=100)
    category_id: int = Field(...)

    class Config:
        from_attributes = True



class PostOrders(BaseModel):
    id: int = Field(...)
    order_date: str = Field(..., max_length=100)
    customer_id: int = Field(...)
    total_amount: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostCategories(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostOrderItems(BaseModel):
    id: int = Field(...)
    order_id: int = Field(...)
    product_id: int = Field(...)
    quantity: int = Field(...)

    class Config:
        from_attributes = True

