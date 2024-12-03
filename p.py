import sqlite3
from datetime import datetime
import tabulate
con=sqlite3.connect('spent.db')
c=con.cursor()
def init():
    c.execute('CREATE TABLE IF NOT EXISTS  spent(price INTEGER, name  TEXT COLLATE NOCASE, massage TEXT, date INTEGER)')
    con.commit()
    con.close()
def add(price,name,massage=''):
    date=str(datetime.now().strftime('%Y - %m - %d | %H:%M'))
    c.execute('INSERT INTO spent VALUES(:price, :name , :massage, :date)',{'price':price, 'name':name ,'massage':massage,'date':date})
    con.commit()
    con.close()
# def insert_st(st):
#     with conn:
#         date=STR(datetime.now().strftime('%Y - %m - %d | %H:%M'))
#         c.execute('INSERT INTO spent VALUES(:price, :name, :date)',{'price':st.price, 'name':st.name ,'date':st.date})
# class sss():
#     def __init__(self,price,name):
#         self.price=price
#         self.name=name

def show(name=None):
    if name:
        c.execute('SELECT * FROM spent WHERE name = (:name)',{'name':name})
        results=c.fetchall()
        c.execute('SELECT sum(price) FROM spent WHERE name = (:name)',{'name':name})
        total_price=c.fetchone()[0]
    else:
        c.execute('SELECT * FROM spent')
        results=c.fetchall()
        c.execute('SELECT sum(price) FROM spent')
        total_price=c.fetchone()[0]
    return total_price,results
    con.close()
def remove(name):
    c.execute('DELETE FROM spent WHERE name = (:name)',{'name':name})
    con.commit()
    con.close()

def update(price,name):
    nprice=400
    c.execute('''UPDATE spent SET price = (:price) WHERE name = (:name)''',{'price':price , 'name':name})
    con.commit()
    con.close()

#init()
#add(500,'snap')
# remove('snap')
#update('snap')
#print(show())
#update(1000,'snap')
#print(show())