from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/products/')
async def get_products(db: Session = Depends(get_db)):
    try:
        return await service.get_products(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/file_upload')
async def post_file_upload(doc: UploadFile, extension: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_file_upload(db, doc, extension)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/products/id')
async def get_products_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_products_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/products/')
async def post_products(raw_data: schemas.PostProducts, db: Session = Depends(get_db)):
    try:
        return await service.post_products(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/products/id/')
async def put_products_id(id: int, name: Annotated[str, Query(max_length=100)], description: Annotated[str, Query(max_length=100)], price: Annotated[str, Query(max_length=100)], category_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_products_id(db, id, name, description, price, category_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/')
async def get_customers(db: Session = Depends(get_db)):
    try:
        return await service.get_customers(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/customers/')
async def post_customers(id: int, name: Annotated[str, Query(max_length=100, pattern="^[A-Z][a-z]+([ '-][A-Z][a-z]+)*$")], address: Annotated[str, Query(max_length=50, pattern='^\\d{1,5}[\\w\\s\\-,.#/]+$')], contact_details: Annotated[str, Query(max_length=10, pattern='^\\d{10,15}$')], db: Session = Depends(get_db)):
    try:
        return await service.post_customers(db, id, name, address, contact_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/profile')
async def post_profile(name: Annotated[str, Query(max_length=101, pattern="^[a-zA-Z]+(?:[ '-][a-zA-Z]+)*$")], email: Annotated[str, Query(max_length=101, pattern='[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}')], phone_no: int, address: Annotated[str, Query(max_length=11)], id: int, db: Session = Depends(get_db)):
    try:
        return await service.post_profile(db, name, email, phone_no, address, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/orders/')
async def post_orders(raw_data: schemas.PostOrders, db: Session = Depends(get_db)):
    try:
        return await service.post_orders(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/products/id')
async def delete_products_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_products_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/categories/')
async def get_categories(db: Session = Depends(get_db)):
    try:
        return await service.get_categories(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/categories/id')
async def get_categories_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_categories_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/categories/')
async def post_categories(raw_data: schemas.PostCategories, db: Session = Depends(get_db)):
    try:
        return await service.post_categories(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/categories/id/')
async def put_categories_id(id: int, name: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_categories_id(db, id, name)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/categories/id')
async def delete_categories_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_categories_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/id')
async def get_customers_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_customers_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/customers/id/')
async def put_customers_id(id: int, name: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_customers_id(db, id, name, address, contact_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/customers/id')
async def delete_customers_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_customers_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/')
async def get_orders(db: Session = Depends(get_db)):
    try:
        return await service.get_orders(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/id')
async def get_orders_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_orders_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/orders/id/')
async def put_orders_id(id: int, order_date: Annotated[str, Query(max_length=100)], customer_id: int, total_amount: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_orders_id(db, id, order_date, customer_id, total_amount)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/orders/id')
async def delete_orders_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_orders_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/order_items/')
async def get_order_items(db: Session = Depends(get_db)):
    try:
        return await service.get_order_items(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/order_items/id')
async def get_order_items_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_order_items_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/order_items/')
async def post_order_items(raw_data: schemas.PostOrderItems, db: Session = Depends(get_db)):
    try:
        return await service.post_order_items(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/order_items/id/')
async def put_order_items_id(id: int, order_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    try:
        return await service.put_order_items_id(db, id, order_id, product_id, quantity)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/order_items/id')
async def delete_order_items_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_order_items_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

