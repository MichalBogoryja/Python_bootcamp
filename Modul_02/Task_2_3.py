# Zadanie 1

name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
name_dictionary = {}

for name in name_list:
    name_dictionary[name] = len(name)

report = f"Zadanie#1\n{name_dictionary}\n\n"

# Zadanie 2
number_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
limit = 21
prime_numbers = []
substracted_list = number_list.copy()

for i in range(limit+1):
    if i == 0 or i == 1:
        if i in substracted_list:
            substracted_list.remove(i)
    else:
        for x in range (2,i):
            if i % x == 0:
                if i in substracted_list:
                    substracted_list.remove(i)
                break
        else:
            prime_numbers.append(i)

report += f"Zadanie#2\n{substracted_list}\n\n"

# Zadanie 3
week_list = ['pon','śro','pią','sob']
full_week_list = ['pon','wto','śro','czw','pią','sob','nie']

for i, day in enumerate(full_week_list):
    if day not in week_list:
        week_list.insert(i,day)

report += f"Zadanie#3\n{week_list}\n\n"

# Zadanie 4
tea = dict()
tea[4] = "wyjmij kubek"
tea[1] = "włącz czajnik"
tea[6] = "włóż herbatę do kubka"
tea[2] = "znajdź opakowanie herbaty"
tea[3] = "zalej herbatę"
tea[5] = "nalej wody do czajnika"
procedure = ''

for step in sorted(tea.items()):
    procedure += f"{step[0]}: {step[1]}\n"

report += f"Zadanie#4\n{procedure}\n\n"

print(report)