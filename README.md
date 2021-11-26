

# Microservice with Django REST framework

### Descripcion Y Contexto

Este proyecto esta desarrollando en el lengauje Python usando el Framework de Django Rest. Se realizara un crud de Categorias, Productos e Items.


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




## Category

### GET

List Category

Request 

    --http://127.0.0.1:8000/petStore/category/
 
Response 
 
```
[
    {
        "id": 1,
        "description": "Large Angelfish"
    },
    {
        "id": 2,
        "description": "Dogs"
    },
  ]
```
    
 List Category By Id
 
 Request GET
 
    --http://127.0.0.1:8000/petStore/category/
    
Response

```
{
    "id": 2,
    "description": "Dogs"
}
   
 ```
   
### POST

Request 

```
  --http://127.0.0.1:8000/petStore/category/2/
  
   {
        "description": "CategoryExample"
    }

```

### DELETE

Request 

```
    http://127.0.0.1:8000/petStore/category/2/
    
```


## Product

### GET

List Products

Request 

    --http://127.0.0.1:8000/petStore/product/
    
Response

```
[
[
    {
        "id": 1,
        "category": {
            "id": 2,
            "description": "Dogs"
        },
        "name": "Godzilla",
        "description": "Aquatic animal"
    },
    {
        "id": 2,
        "category": {
            "id": 1,
            "description": "Large Angelfish"
        },
        "name": "ziberan",
        "description": "Aquatic animal"
    }
]
]

```

List Product by Id


Request 

    --http://127.0.0.1:8000/petStore/product/1/
    
    
Response

```
{
    "id": 1,
    "name": "Angelfish",
    "description": "Aquatic animal",
    "categoy": 1
}

```


### POST 


Request
```
http://127.0.0.1:8000/petStore/product/1/

{
    "name": "Godzilla",
    "description": "Aquatic animal",
    "categoy": 2
}

```


## Item

### GET

Request 

```
      http://127.0.0.1:8000/petStore/item/
[
    {
        "id": 2,
        "image": "/archivos/975de4e0-3832-4e57-a81c-53b11f847ee1.jpg",
        "product": {
            "id": 1,
            "category": {
                "id": 2,
                "description": "Dogs"
            },
            "name": "Godzilla",
            "description": "Aquatic animal"
        },
        "description": "Large Angelfish3",
        "quantity": 2,
        "price": 2400.0
    }  
]

```
### PUT

Request


```
      http://127.0.0.1:8000/petStore/item/2

{
  
    "quantity": 30

}
```
