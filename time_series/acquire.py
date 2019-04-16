import requests
import pandas as pd
import json

def get_items():
    base_url = 'https://python.zach.lol'
    response = requests.get(base_url + '/api/v1/items')
    data = response.json()
    items = data['payload']['items']
    while data['payload']['page'] < 4:
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        items += data['payload']['items']
        if data['payload']['next_page'] == None:
            break
    return pd.DataFrame(items)

def get_stores():
    base_url = 'https://python.zach.lol'
    response = requests.get(base_url + '/api/v1/stores')
    data = response.json()
    stores = data['payload']['stores']
    return pd.DataFrame(stores)

def get_sales():
    base_url = 'https://python.zach.lol'
    response = requests.get(base_url + '/api/v1/sales')
    data = response.json()
    sales = data['payload']['sales']
    while data['payload']['page'] < 184:
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        sales += data['payload']['sales']
        if data['payload']['next_page'] == None:
            break
    return pd.DataFrame(sales)