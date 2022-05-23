import eel
import sqlite3

"""
Author: https://github.com/akula12345
"""
@eel.expose
def auth(login, password):
	if login == "test" and  password == "test":
		return "Данні вірні!"
	else:
		return "Невірні данні!"

def checkdb():
	db = sqlite3.connect('shop.db')
	sql = db.cursor()
	sql.execute("""CREATE TABLE IF NOT EXISTS shopping (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameproduct TEXT,
    size TEXT,
    amount INT,
    price INT
)
""")
	sql.execute("""CREATE TABLE IF NOT EXISTS sale (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameproduct TEXT,
    size TEXT,
    amount INT,
    price INT
)
""")
	sql.close()

@eel.expose
def addshopping(namep, sizep, amountp, pricep):
	try:
		checkdb()
		db = sqlite3.connect('shop.db')
		sql = db.cursor()
		sql.execute(f'INSERT INTO shopping(nameproduct, size, amount, price) VALUES (?, ?, ?, ?)', (namep, sizep, amountp, pricep))
		db.commit()
		sql.close()

		return "Товар був доданний до закупівлі!"
	except:
		return "Помилка! :("


@eel.expose
def addsale(namep, sizep, amountp, pricep):
	try:
		checkdb()
		db = sqlite3.connect('shop.db')
		sql = db.cursor()
		sql.execute(f'INSERT INTO sale(nameproduct, size, amount, price) VALUES (?, ?, ?, ?)', (namep, sizep, amountp, pricep))
		db.commit()
		sql.close()

		return "Товар був доданний до продажу!"
	except:
		return "Помилка! :("

@eel.expose
def analyticsShopping():
	try:
		checkdb()
		db = sqlite3.connect('shop.db')
		sql = db.cursor()
		shopping = []
		for i in sql.execute('SELECT * FROM shopping'):
			shopping += [i]
		sql.close()
		return shopping
	except:
		return "Помилка!"

@eel.expose
def analyticsSale():
	try:
		checkdb()
		db = sqlite3.connect('shop.db')
		sql = db.cursor()
		sale = []
		for i in sql.execute('SELECT * FROM sale'):
			sale += [i]
		sql.close()
		return sale
	except:
		return "Помилка!"

@eel.expose
def analytics():
	try:
		checkdb()
		db = sqlite3.connect('shop.db')
		sql = db.cursor()
		shopping = 0
		sale = 0
		res = 0
		for i in sql.execute('SELECT amount, price FROM shopping'):
			shopping += i[0] * i[1]
		for i in sql.execute('SELECT amount, price FROM sale'):
			sale += i[0] * i[1]
		sql.close()
		res = sale - shopping
		return [shopping, sale, res]
	except:
		return "Помилка!"

eel.init("web")


eel.start("main.html", size=(1280, 720))