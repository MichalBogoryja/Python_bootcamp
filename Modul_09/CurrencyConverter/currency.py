import requests
import csv

from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)


def get_data():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/"
                            "C?format=json")
    data = response.json()
    return data


def save_to_file():
    data = get_data()
    currencies = data[0]['rates']
    with open('currencies.csv', mode='w', newline='\n') as csv_file:
        fieldnames = ['currency', 'code', 'bid', 'ask']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for currency in currencies:
            writer.writerow(currency)
    csv_file.close()


def extract_data(code):
    with open('currencies.csv', mode='r') as csv_file:
        for line in csv_file:
            if f';{code};' in line:
                data = line
                csv_file.close()
                return data
        else:
            csv_file.close()
            print(f'There is no such ({code}) currency')


def currencies_codes():
    data = get_data()
    currencies = data[0]['rates']
    codes = []
    for currency in currencies:
        codes.append(currency["code"])
    return codes


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        save_to_file()
        currencies_list = currencies_codes()
        return render_template("currency.html", codes=currencies_list)
    elif request.method == 'POST':
        received_message = request.form
        print(f'''Received message: {received_message['message']}''')
        return redirect("/calculator")


@app.route('/result', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        received_message = request.args.to_dict()
        save_to_file()
        currencies_list = currencies_codes()
        currency = extract_data(received_message["currency"]).split(";")
        print(type(currency))
        bid = currency[2]
        ask = currency[3]
        return render_template("result.html", codes=currencies_list,
                               message=received_message, bid=bid, ask=ask)
    elif request.method == 'POST':
        received_message = request.form
        print(f'''Received message: {received_message['message']}''')
        return redirect("/calculator")