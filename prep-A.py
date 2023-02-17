#Crea un programma che crei un DB chiamato Animali, contenente una tabella Mammiferi con i seguenti campi Id,Nome_Proprio (varchar),Razza (varchar),Peso (int),Eta (int)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Animali")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE  (name VARCHAR(255), address VARCHAR(255))")
