from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('D:/Flask22/phonebook/phonebook.db')

cur = connection.cursor()
cur.execute("create table users ( id integer primary key autoincrement, firstname text not null, lastname text not null, number integer not null)")
