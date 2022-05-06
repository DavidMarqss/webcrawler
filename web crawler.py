#Bibliotecas
import requests
import schedule
import time
from datetime import datetime
from bs4 import BeautifulSoup

#Função
def job(): 
    urla = requests.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/%27')
    html1 = urla.content
    site = BeautifulSoup(html1, 'html.parser')
    valor = site.find('div', attrs={'class':'priceValue smallerPrice'})
    
    vf = valor.find('span')
    data = datetime.now()
    bitcoin = [vf.text, str(data)]

    print()
    print(bitcoin)
    print()

#Repetir a cada (x) minutos
schedule.every(2).minutes.do(job)
while True:
    schedule.run_pending()
    