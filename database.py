from multiprocessing import connection
import sqlite3
from flask import g

# connection = sqlite3.connect('D:/Flask22/phonebook/phonebook.db')

# cur = connection.cursor()
# cur.execute("create table users ( id integer primary key autoincrement, firstname text not null, lastname text not null, number integer not null)")

def connect_to_database():
    sql = sqlite3.connect('D:/Flask22/phonebook/phonebook.db')
    sql.row_factory = sqlite3.Row
    return sql

def getDatabase():
    if not hasattr(g, "phonebook_db"):
        g.phonebook_db = connect_to_database()
    return g.phonebook_db    

