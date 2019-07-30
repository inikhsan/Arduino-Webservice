import serial

#from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='speedometer')
cursor = cnx.cursor()

skrg = datetime.now()

ser = serial.Serial('COM4', 9600)
temp = ''
while 1:
	data=ser.readline().rstrip('\n')
	#print data
	data=data.strip()
	
	info = data
	databaru = info.split(",")

	print databaru[0] 
	print databaru[1] 
	
	#print ('--'+ data)
	
	add_logdata = ("INSERT INTO kecepatan "
               "(spid, speed, tanggal) "
               "VALUES (%s, %s, %s)")

	dataB = (databaru[0], databaru[1], skrg)
	
	
	if (int(databaru[1]) >= 30):
	# Insert new employee
		cursor.execute(add_logdata, dataB)

	# Make sure data is committed to the database
	cnx.commit()
	
cursor.close()
cnx.close()