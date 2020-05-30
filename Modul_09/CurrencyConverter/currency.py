import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
currencies = data[0]['rates']

with open('currencies.csv', mode='w', newline='\n') as csv_file:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";")

    writer.writeheader()
    for currency in currencies:
        writer.writerow(currency)
