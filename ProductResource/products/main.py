import requests


PRODUCTS_URL = "http://127.0.0.1:8000/products/"

response = requests.get(PRODUCTS_URL)


products = response.text

# print(response.status_code)
print(products)