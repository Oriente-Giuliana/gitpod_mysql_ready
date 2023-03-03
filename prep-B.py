#
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_proprio,Razza,Peso,Eta) VALUES ( %s,%s,%s,%s)"
val = [
("leone","felidi","190","5")
("")

mycursor.execute(sql, val)

mydb.commit()


