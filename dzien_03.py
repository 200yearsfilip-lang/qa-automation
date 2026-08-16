# 1
tested_markets = ["pl", "de", "cz", "sk"]
print(tested_markets[0])
print(tested_markets[-1])
print(len(tested_markets))

# 2
tested_markets.append("ua")
print("cz" in tested_markets)

# 3
api_response = {
    "status": 200,
    "market": "pl",
    "products": [
        {"id": 1, "name": "Watch 7", "price": 1399.00, "in_stock": True},
        {"id": 2, "name": "Watch 7 Ultra", "price": 2999.99, "in_stock": True},
        {"id": 3, "name": "Watch 6 Ultra", "price": 2000.00, "in_stock": False},
    ],
}

# 4
print(api_response["products"][1]["name"])

# 5
for product in api_response["products"]:
    if product["in_stock"]:
        print(f"{product['name']} - {product['price']} zł - dostępny")
    else:
        print(f"{product['name']} - {product['price']} zł - niedostępny")

# 6
print(api_response.get("error_message"))

# 7
available = 0
for product in api_response["products"]:
    if product["in_stock"]:
        available += 1

print(f"Dostępne produkty: {available} z {len(api_response['products'])} ")
