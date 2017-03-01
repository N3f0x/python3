import ipaddress
import os
import time
import ftplib
import random

#Skapar en lista som heter iplist
iplist = []

#Gör en range från 1 - 1000
xrange = range(1,1000)

#itirerar loopen en gång för varje värde i xrange.
for i in xrange:
#Sätter IP till 10.
  ip = "10."
#Randomizar ett värde emellan 0 och 255 och lägger till det på IP. Detta görs tre gånger för att få en fullständig IP-adress.
  ip += ".".join(map(str, (random.randint(0, 255)
                          for i in range(3))))
#Sparar IP-adresserna i en lista som heter iplist.
  iplist.append(ip)

#Kör loopen en gång för varje värde i xrange.
for ip_address in iplist:
		#Kör kommandot innanför "" i cmd och tar den första ip-adressen i iplist.
		os.system("netsh interface ipv4 set address \"Local Area Connection 3\" static {} 255.0.0.0 10.0.0.1".format(ip_address))
		print("netsh interface ipv4 set address \"Local Area Connection 3\" {} static 255.0.0.0 10.0.0.1".format(ip_address))

		#Väntar 5 sekunder innan den kör om loopen.
		time.sleep(5)

		#Connectar till FTP med oskar som användare och orre som lösenord och sänder en fil. !OBS! ändra server_address till serverns statiska IP.
		os.system("""\@echo off
		echo user oskar> ftpcmd.dat
		echo orre>> ftpcmd.dat
		echo bin>> ftpcmd.dat
		echo put %1>> ftpcmd.dat
		echo quit>> ftpcmd.dat
		ftp -n -s:ftpcmd.dat {}
		del ftpcmd.dat""".format(server_address))
