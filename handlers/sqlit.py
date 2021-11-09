import sqlite3
import datetime

def startbot():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    db.commit()
