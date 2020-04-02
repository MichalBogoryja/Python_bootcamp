roquefort = 12.50
stilton = 11.24
brie = 9
gouda = 8.55
edam = 11.5
parmezan = 16.50
mozzarella = 14
goat_cheese = 122.32
camembert = 0

longest_name = 0
max_price = 0

cheeses = [['roquefort', roquefort], ['stilton', stilton], ['brie', brie], ['gouda', gouda], ['edam', edam],
           ['parmezan', parmezan], ['mozzarella', mozzarella], ['goat_cheese', goat_cheese], ['camembert', camembert]]

for cheese in cheeses:
    name_length = len(cheese[0])
    price = cheese[1]
    if name_length > longest_name:
        longest_name = name_length
    if price > max_price:
        max_price = price

report = f"Raport z zakupow sera:\n"

for cheese in cheeses:
    price = cheese[1]
    name_length = len(cheese[0])
    if price != 0:
        report += f"Kupiono {cheese[0]:<{longest_name}} w cenie {price:>{len(str(max_price))}.2f} zł.\n"
    else:
        report += f"{'Sera':7} {cheese[0]:{longest_name}} nie udało sie znaleźć.\n"

print(report)