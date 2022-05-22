import requests
import schedule
import json
import time
from datetime import datetime
from bs4 import BeautifulSoup

def job(): 

    url1 = requests.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/')
    htmlBruto = url1.content
    site = BeautifulSoup(htmlBruto, 'html.parser')
    tagPreco = site.find('div', attrs={'class':'priceValue smallerPrice'})
    preco = tagPreco.find('span')
    time = str(datetime.now())
    
    url = "https://data.mongodb-api.com/app/data-sqeua/endpoint/data/beta/action/insertOne"
    payload = json.dumps({
        "collection": "coin",
        "database": "datacointeste",
        "dataSource": "Testexd",
        "document": {
            "preço": preco.text,
            "horario": time
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'qmPB5eyfOAamg1P4zbQZFK1JxyVUVBRoTD9wdMXHgZyGgGpzMN58zlKJIgGAODlV'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(0)