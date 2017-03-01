
import ipaddress
import os
import time
from ftplib import FTP


file = open("bla.txt", "rb")
server = '172.16.1.10'
raknare = 1

with open("IP-list.txt", "r") as listfil:

	for ip_address in listfil:

		os.system("netsh interface ipv4 set address \"Local Area Connection 3\" static {} 255.0.0.0 10.0.0.1".format(ip_address))
		print("netsh interface ipv4 set address \"Local Area Connection 3\" {} static 255.0.0.0 10.0.0.1".format(ip_address))
		print ("Steg {} av 1000,".format(raknare))
		raknare = raknare + 1
		time.sleep(3.5)
		FTP1 = FTP(server)
		FTP1.login("oskar", "cisco")
		FTP1.storbinary("STOR bla.txt", file)
		FTP1.quit()
