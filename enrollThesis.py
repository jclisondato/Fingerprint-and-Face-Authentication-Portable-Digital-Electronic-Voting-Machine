from pyfingerprint.pyfingerprint import PyFingerprint
import sqlite3
import pyfingerprint
import hashlib
import sys


conn = sqlite3.connect('voting_database.db')
curs = conn.cursor()
value = "2"
curs.execute('DELETE FROM voters WHERE position=? ',value)

conn.commit()