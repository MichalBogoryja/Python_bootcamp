roquefort = ['roquefort', 12.50, 2]
stilton = ['stilton', 11.24, 1]
brie = ['brie', 9, 1]
gouda = ['gouda', 8.55, 1]
edam = ['edam', 11.5, 1]
parmezan = ['parmezan', 16.50, 3.5]
mozzarella = ['mozzarella', 14, 0.13]
goat_cheese = ['goat_cheese', 122.32, 0.22]
camembert = ['camembert', 0, 0]
mint_leaf = ['mint leaf', 100, 0.2]

longest_name = 0
longest_price = 0
longest_cost = 0

total_cost = 0

cheeses = [roquefort, stilton, brie, gouda, edam, parmezan,
           mozzarella, goat_cheese, camembert, mint_leaf]

for cheese in cheeses:
    cheese.append(cheese[1] * cheese[2])
    name_length = len(cheese[0])
    price = cheese[1]
    cost = cheese[3]
    if name_length > longest_name:
        longest_name = name_length
    if price > longest_price:
        longest_price = int(price)
    if cost > longest_cost:
        longest_cost = int(cost)

report = f"Raport z zakupow sera:\n"

for cheese in cheeses:
    price = cheese[1]
    name_length = len(cheese[0])
    if price != 0:
        report += f"Kupiono {cheese[2]:>4.2f} kg {cheese[0]:<{longest_name}} cena: {price:>{len(str(longest_price)) + 3}.2f}" \
                 f" zł/kg, koszt: {cheese[3]:>{len(str(longest_cost)) + 3}.2f} zł.\n"
        total_cost += cheese[3]
    else:
        report += f"{'Sera':7} {cheese[0]:{longest_name}} nie udało sie znaleźć.\n"

report += f"\nŁącznie wydano: {total_cost:.2f} zł."
print(report)

