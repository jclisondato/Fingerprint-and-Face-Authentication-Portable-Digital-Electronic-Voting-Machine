import sqlite3
import pyrebase
import csv
import pandas as pd
from urllib import request
from printertest import totalVotes
config = {
  "apiKey": "AIzaSyCeHmYk0JWMGrqaY7zE12TagjEklxdH8ME",
  "authDomain": "evmthesis.firebaseapp.com",
  "databaseURL": "https://evmthesis-default-rtdb.firebaseio.com",
  "projectId": "evmthesis",
  "storageBucket": "evmthesis.appspot.com",
  "messagingSenderId": "762023483827",
  "appId": "1:762023483827:web:eef8e7b36420e575fc53c6",
  "measurementId": "G-0941KERDG6"
}

firebase=pyrebase.initialize_app(config)
db = firebase.database()

conn = sqlite3.connect('voting_database.db')
curs = conn.cursor()

def checkAlreadyVoted(posnumber):
  for result in db.child("thesis").get().each():
    for pos in db.child("thesis").child(result.key()).get():
      if pos.val() == posnumber:
        return True

def checkAlreadyVotedName(name):
  for result in db.child("thesis").get().each():
      if result.key() == name:
        return True


def finalizeFire(name,pos,pres,vice,sec,trea):
    posdata = {"pos": pos}
    data = {"pres": pres, "vice": vice, "sec": sec, "trea": trea}
    db.child("thesis").child(name).set(posdata)
    db.child("thesis").child(name).child('selection').set(data)
    print('DONE!')


def getDataFiretoSQL():
  data = []
  for result in db.child("thesis").get():
    if result.key() != "zero zero":
      dataParent = []
      for pos in db.child("thesis").child(result.key()).get():
        if pos.key() == "pos":
          dataParent.append(result.key())
          dataParent.append(pos.val())

          for selection in db.child("thesis").child(result.key()).child("selection").get():
            dataParent.append(selection.val())
          data.append(dataParent)
  return data

def updateFiretoSql():
  data = getDataFiretoSQL()
  curs.execute("DELETE FROM syncvotes;")
  sql = """INSERT INTO syncvotes(name,pos,pres,vice,sec,trea) VALUES(?,?,?,?,?,?);"""
  curs.executemany(sql, data)
  conn.commit()
  print("Firebase data updated to SQL syncvotes")           # sync firebase and sql


def votecountsPrintCSV():
  sqlquery = "SELECT * FROM syncvotes"
  curs.execute(sqlquery)
  for row in curs.fetchall():
    df = pd.read_sql_query(sqlquery, conn)
    df.to_csv('votes.csv', index=False)   #microsoft excel file

def voteCounts():
  presA = []
  viceB = []
  secC = []
  treaD = []
  curs.execute("SELECT pres,vice,sec,trea FROM syncvotes")
  for pres,vice,sec,trea in curs.fetchall():
    presA.append(pres)
    viceB.append(vice)
    secC.append(sec)
    treaD.append(trea)
  A = {x: presA.count(x) for x in presA}
  B = {x: viceB.count(x) for x in viceB}
  C = {x: secC.count(x) for x in secC}
  D = {x: treaD.count(x) for x in treaD}
  totalVotes(A,B,C,D)           ## to print the tally


# def testConnection():
#   try:
#     request.urlopen("https://www.google.com/", timeout=5)
#     print("Connected to Internet")
#   except:
#     print("No Internet Connection")

