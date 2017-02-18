# basics from Sqlite creating db, adding stuff, update and delete/ draw to matplotlib
import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

style.use('fivethirtyeight')

conn = sqlite3.connect('testing.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tablename(key0 REAL,key1 TEXT,key2 TEXT,val REAL)')


def data_entry():
    c.execute('INSERT INTO tablename VALUES("firstkey","secondkey",404)')
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    data_key0 = time.time()
    date_key1 = str(datetime.datetime.fromtimestamp(data_key0).strftime('%d-%m-%Y %H:%M:%S'))
    data_key2 = 'python'
    data_val = random.randrange(5, 55)
    c.execute('INSERT INTO tablename (key0,key1,key2,val) VALUES (?, ?, ?, ?)',
              (data_key0, date_key1, data_key2, data_val))
    conn.commit()


def read_from_db():
    c.execute('SELECT key1, val FROM tablename WHERE val > 25')
    cpdata = c.fetchall()
    for row in cpdata:
        print(row)


def graph_data():
    c.execute('SELECT key0,val FROM tablename')
    cpdata = c.fetchall()
    dates = []
    values = []
    for row in cpdata:
        # print(row)
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


def del_and_update():
    c.execute('SELECT * FROM tablename')
    [print(row) for row in c.fetchall()]

    c.execute('UPDATE tablename SET val = 99 WHERE val=7')
    conn.commit()


    c.execute('DELETE from tablename WHERE val = 99')
    conn.commit()

    c.execute('SELECT * FROM tablename')
    [print(row) for row in c.fetchall()]


# create_table()
# data_entry()
#
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)

# read_from_db()
# graph_data()
del_and_update()

c.close()
conn.close()
