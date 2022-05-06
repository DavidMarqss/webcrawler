#Bibliotecas
import requests
import json

#Conexão com o Mongodb
url = "https://data.mongodb-api.com/app/data-sqeua/endpoint/data/beta/action/insertOne"

payload = json.dumps({
    "collection": "coin",
    "database": "datacointeste",
    "dataSource": "Testexd",
    "document": {
         "Nome": "Testezin"
    
    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'qmPB5eyfOAamg1P4zbQZFK1JxyVUVBRoTD9wdMXHgZyGgGpzMN58zlKJIgGAODlV'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
