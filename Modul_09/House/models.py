import json


class Finances:
    def __init__(self):
        try:
            with open("finances.json", "r") as f:
                self.finances = json.load(f)
        except FileNotFoundError:
            self.finances = []

    def all(self):
        return self.finances

    def get(self, id):
        finance = [finance for finance in self.all() if finance['id'] == id]
        if finance:
            return finance[0]
        return []

    def create(self, data):
        self.finances.append(data)
        self.save_all()

    def save_all(self):
        with open("finances.json", "w") as f:
            json.dump(self.finances, f)

    def update(self, id, data):
        finance = self.get(id)
        if finance:
            index = self.finances.index(finance)
            self.finances[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        finance = self.get(id)
        if finance:
            self.finances.remove(finance)
            self.save_all()
            return True
        return False

    def count_budget(self, category="total"):
        finance = self.finances
        result = {}
        result[category] = {}
        result[category]["Zysk"] = 0
        result[category]["Koszty"] = 0
        for fin in finance:
            if category == "total" or fin["kategoria"] == category:
                if fin["przychod"]:
                    result[category]["Zysk"] += fin["kwota"]
                else:
                    result[category]["Koszty"] += fin["kwota"]
        return result

    def categories(self):
        finance = self.finances
        categories = set()
        result = {}
        for fin in finance:
            categories.add(fin["kategoria"])
        for category in categories:
            finance = self.count_budget(category)
            result[category] = finance[category]
        result = sorted(result.items(), key = lambda x: x[1]["Koszty"])
        return result


finances = Finances()
