

# Microservice with Django REST framework

### Descripcion Y Contexto

Este proyecto esta desarrollando en el lengauje Python usando el Framework de Django Rest.

### Requeriments

- asgiref==3.4.1
- backports.entry-points-selectable==1.1.0
- certifi==2021.5.30
- click==8.0.1
- colorama==0.4.4
- distlib==0.3.2
- Django==3.2.7
- filelock==3.0.12
- Flask==2.0.1
- itsdangerous==2.0.1
- Jinja2==3.0.1
- MarkupSafe==2.0.1
- mysql==0.0.3
- mysqlclient==2.0.3
- pipenv==2021.5.29
- platformdirs==2.3.0
- psycopg2==2.9.1
- pytz==2021.1
- six==1.16.0
- sqlparse==0.4.2
- virtualenv==20.7.2
- virtualenv-clone==0.5.7
- Werkzeug==2.0.1
- djangorestframework
- django-simple-history
- django-cors-headers
- django-extra-fields==0.3
- Pillow




## Shopping cart

### GET

List Shopping cart
Request 

    --http://localhost:8000/api/v1/cart/
 
Response 
 
```
[
    {
        "id": 2,
        "customerId": "pepe2@hotmail",
        "item_id": 5,
        "quantity": 80,
        "price": 24.0
    }
]
```
    
 List  Shopping cart by email
 
 Request GET
 
    --http://127.0.0.1:8000/petStore/category/
    
Response

```
    {
        "item_id": 5,
        "quantity": 80,
        "price": 24.0
    }
   
 ```
   
### POST

Request 

```
  --http://localhost:8000/api/v1/cart/
  
    {

        "customerId": "pepe@hotmail",
        "item_id": 5,
        "quantity": 80,
        "price": 24.0
    }

```

### DELETE

Request 

```
    http://localhost:8000/api/v1/cart?customerId=pepito@gmail.com&item_id=5  
    
```


### CLEAR


Request 

    --http://localhost:8000/api/v1/cart/clear/:customerId
    
