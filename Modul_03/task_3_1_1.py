shops = dict()

shops["piekarnia"] = ['chleb', 'Pączek', 'Bułki']
shops["warzywniak"] = ['marchew', 'seler', 'Rukola']

result = "Lista zakupów\n"
total = 0

for i, shop in enumerate(shops):
    products = [product.capitalize() for product in shops[shop]]
    total += len(products)
    if i == 0:
        result += "Pierwszy "
    elif i == 1:
        result += "Drugi "
    else:
        result += "Kolejny "
    result += f"sklep to {shop.capitalize()}, kupuje tu: {products}\n"

result += f"W sumie kupuję {total} produktów."
print(result)