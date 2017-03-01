import ipaddress
import os
import time
import ftplib


server_network = ipaddress.ip_network("192.168.16.0/24")
client_network = ipaddress.ip_network("192.168.17.0/24")

for client_address, server_address in zip(client_network.hosts(), server_network.hosts()):
		#Kör kommandot innanför "" i cmd och ändrar IP på datorn enligt listan i client_network.
		os.system("netsh interface ipv4 set address \"Local Area Connection 3\" static {} 255.255.255.0 192.168.16.1".format(client_address))
		print("netsh interface ipv4 set address \"Local Area Connection 3\" {} static 255.255.255.0 192.168.16.1".format(client_address))
		#Connectar till FTP med Oskar som användare och orre som lösenord och för över en fil.
		os.system("""\@echo off 
		echo user oskar> ftpcmd.dat
		echo orre>> ftpcmd.dat
		echo bin>> ftpcmd.dat
		echo put %1>> ftpcmd.dat
		echo quit>> ftpcmd.dat
		ftp -n -s:ftpcmd.dat {}
		del ftpcmd.dat""".format(server_address))
		#Väntar 5 sekunder innan den kör om loopen.
		time.sleep(5)


		#PUT FTP GREJ
