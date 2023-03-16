import json


def write_order_to_json(product, quantity, price, buyer, date):
    order = {
        "product": product,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('orders.json', 'r+') as f:
        data = json.load(f)
        orders = data['orders']
        orders.append(order)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


write_order_to_json('Item 1', 5, 10.99, 'John Doe', '2022-03-16')
