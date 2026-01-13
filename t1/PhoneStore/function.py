
def create(manufactuer, model, price):
    return {
        'manufacturer': manufactuer,
        'model': model,
        'price': price
    }

def create_5_phone_models():

    return[create('Samsung', 'Note 9', 3000),
           create('Samsung', 'Note 10', 3500),
           create('IPhone', 'IPhone X', 5000),
           create('Huawei', 'P 20', 700),
           create('Motorola', 'Edge 60', 2000)
    ]

#1

def add_phone_fun(phone_list, manufactuer, model, price):
    phone_list.append(create(manufactuer, model, price))

#3

def add_price_manufacturer_model_fun(phone_list, manufacturer, model, price):
    for i, a in enumerate(phone_list):
        if a['manufacturer'] == manufacturer and a['model'] == model:
            phone_list[i]['price'] += price

#4
def calculate_percent(percent, price):
    final_price = price * (percent / 100)
    return final_price

def modify_percent_fun(phone_list, precent):
    for i, a in enumerate(phone_list):
        a['price'] += calculate_percent(precent, a['price'])