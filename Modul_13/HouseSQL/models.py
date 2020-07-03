import json
import sqlite3
from sqlite3 import Error

table = "finances"


def create_connection(db_file):
    """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def execute_sql(conn, sql):
    """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


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
        result = sorted(result.items(), key=lambda x: x[1]["Koszty"])
        return result


class FinancesSQL:
    def __init__(self, db_file):
        try:
            conn = create_connection(db_file)
            execute_sql(conn, create_finances_sql)
            self.finances = []
        except FileNotFoundError:
            self.finances = []

    def all(self, db_file):
        conn = create_connection(db_file)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        self.finances = cur.fetchall()
        return self.finances

    def get(self, id, db_file):
        finance = [finance for finance in self.all(db_file)
                   if finance[0] == id]
        if finance:
            return finance[0]
        return []

    def create(self, data, db_file):
        sql = f'''INSERT INTO {table}(title, description, kategoria, kwota,
            przychod) VALUES(?,?,?,?,?)'''
        self.save_all(db_file, sql, data)

    def save_all(self, db_file, sql, data=None):
        conn = create_connection(db_file)
        cur = conn.cursor()
        if data:
            cur.execute(sql, data)
        else:
            cur.execute(sql)
        conn.commit()

    def update(self, id, db_file, **kwargs):
        parameters = [f"{k} = ?" for k, v in kwargs.items() if v is not None]
        parameters = ", ".join(parameters)
        data = tuple(v for v in kwargs.values() if v is not None)
        sql = f''' UPDATE {table} SET {parameters} WHERE id = {id}'''
        self.save_all(db_file, sql, data)
        return True

    def delete(self, id, db_file):
        conn = create_connection(db_file)
        sql = f'DELETE FROM {table} WHERE id={id}'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True

    def count_budget(self, db_file, category="total"):
        finance = self.all(db_file)
        result = {}
        result[category] = {}
        result[category]["Zysk"] = 0
        result[category]["Koszty"] = 0
        for fin in finance:
            if category == "total" or fin[3] == category:
                if fin[5]:
                    result[category]["Zysk"] += fin[4]
                else:
                    result[category]["Koszty"] += fin[4]
        return result

    def categories(self, db_file):
        finance = self.all(db_file)
        categories = set()
        result = {}
        for fin in finance:
            categories.add(fin[3])
        for category in categories:
            finance = self.count_budget(db_file, category)
            result[category] = finance[category]
        result = sorted(result.items(), key=lambda x: x[1]["Koszty"])
        return result


create_finances_sql = """
   -- finances table
   CREATE TABLE IF NOT EXISTS finances (
      id integer PRIMARY KEY,
      title text NOT NULL,
      description text,
      kategoria text,
      kwota real,
      przychod integer
   );
   """

finances = Finances()
financesSQL = FinancesSQL(db_file="database.db")
