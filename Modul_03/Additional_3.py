import copy
import logging
from datetime import datetime

date = str(datetime.now().isoformat(timespec='seconds')).replace(":", "_").replace("T", "__")

logging.basicConfig(filename=f'{date}_cars.log', filemode='w',
                    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

models = ['Volkswagen - Golf', 'Renault - Clio', 'Volkswagen - Polo',
          'Ford - Fiesta', 'Nissan - Qashqai', 'Peugeot - 208', 'VW - Tiguan', 'Skoda - Octavia',
          'Toyota - Yaris', 'Opel - Corsa', 'Dacia - Sandero', 'Renault - Captur', 'Citroen - C3',
          'Peugeot - 3008', 'Ford - Focus', 'Fiat - 500', 'Dacia - Duster', 'Peugeot - 2008',
          'Skoda - Fabia', 'Fiat - Panda', 'Opel - Astra', 'VW - Passat', 'Mercedes-Benz - A-Class',
          'Peugeot - 308', 'Ford - Kuga']

sales2018 = ['445,754', '336,268', '299,920', '270,738', '233,026', '230,049', '224,788',
             '223,352', '217,642', '217,036', '216,306', '214,720', '210,082', '204,197', '196,583',
             '191,205', '182,100', '180,204', '172,511', '168,697', '160,275', '157,986', '156,020',
             '155,925', '154,125']

sales2017 = ['483,105', '327,395', '272,061', '254,539', '247,939', '244,615', '234,916',
             '230,116', '199,182', '232,738', '196,067', '212,768', '207,299', '166,784', '214,661',
             '189,928', 'NA', '180,868', '180,136', '187,322', '217,813', '184,123', 'NA', 'NA', 'NA']

sales2016 = ['492,952', '315,115', '308,561', '300,528', '234,340', '249,047', '180,198',
             '230,255', '193,969', '264,844', '170,300', '217,105', '134,560', 'NA', '214,435',
             '183,730', 'NA', 'NA', '177,301', '191,617', '253,483', '208,575', 'NA', '195,653', 'NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer3_1 = 0
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {}

highest_amount_2017 = 0
highest_brand_2018 = 0
lowest_total = 10000000000
ford_2017 = 0
ford_2018 = 0

for i, type in enumerate(models):
    type = type.split(' - ')
    brand = type[0]
    model = type[1]
    if brand not in cars.keys():
        cars[brand] = {}
    cars[brand][model] = {}
    cars[brand][model]["sales"] = {}
    if sales2016[i] == 'NA':
        sales2016[i] = '0'
    if sales2017[i] == 'NA':
        sales2017[i] = '0'
    price2016 = int(sales2016[i].replace(',', ''))
    price2017 = int(sales2017[i].replace(',', ''))
    price2018 = int(sales2018[i].replace(',', ''))
    cars[brand][model]["sales"]["2016"] = price2016
    cars[brand][model]["sales"]["2017"] = price2017
    cars[brand][model]["sales"]["2018"] = price2018

modified_cars = copy.deepcopy(cars)

for brand, models in modified_cars.items():
    logging.debug(f'Brand of a car: {brand}')
    modified_cars[brand]["total_2018"] = 0
    for model, sales in models.items():
        if model != "total_2018":
            modified_cars[brand]["total_2018"] += int(modified_cars[brand][model]["sales"]["2018"])
            for sale, years in sales.items():
                years["total"] = years["2016"] + years["2017"] + years["2018"]
                if years["2017"] > highest_amount_2017:
                    highest_amount_2017 = years["2017"]
                    answer1 = model
                if years["2016"] == 0 and years["2017"] != 0:
                    answer3.append(model)
                if years["total"] < lowest_total:
                    lowest_total = years["total"]
                    answer4 = model
            if brand == "Ford":
                ford_2017 += years["2017"]
                ford_2018 += years["2018"]
                pass

    if modified_cars[brand]["total_2018"] > highest_brand_2018:
        highest_brand_2018 = modified_cars[brand]["total_2018"]
        answer2 = brand

answer5 = "{:.0%}".format(((ford_2018-ford_2017) / ford_2017))

print(cars)
