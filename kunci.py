import serial
from time import strftime
#from __future__ import print_function
import datetime
from datetime import date, timedelta
import mysql.connector

cnx = mysql.connector.connect(host='us-cdbr-iron-east-02.cleardb.net', user='b44f67710baaf4', password='203a145a', database='heroku_29fdc3ecbc4ef36')
cursor = cnx.cursor()

skrg = datetime.datetime.now()

arduino = serial.Serial('COM7', 115200)
temp = ''
while 1:
	data=arduino.readline()
	# print (data)
	# data=data.strip()
	
	databaru = data.split()

	print (databaru[0]) 

	#print ('--'+ data)
	
	add_logdata = ("INSERT INTO tap (id_pengguna, tanggal) VALUES (%s, %s)") 		
		
	dataB = (databaru[0], skrg)


	if (str(databaru[0])):
	# # Insert new employee
	 	cursor.execute(add_logdata, dataB)

	# Make sure data is committed to the database
	cnx.commit()
	
cursor.close()
cnx.close()