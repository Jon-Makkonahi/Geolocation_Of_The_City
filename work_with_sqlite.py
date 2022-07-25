import os
import sqlite3

from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
ADDRESS = os.getenv('ADDRESS', default='address')
LANGUAGE = 'ru'

connection = sqlite3.connect('sqlite3.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sqlite3
              (Token TEXT, URL TEXT, Language TEXT)''')

cursor.execute(
    f"INSERT INTO sqlite3 VALUES ('{TOKEN}', '{ADDRESS}', '{LANGUAGE}')")

cursor.execute("SELECT * FROM sqlite3")
token, url, language = (cursor.fetchone())

connection.commit()
connection.close()
