from ftplib import FTP_TLS
from ftplib import FTP
import os
import time
import ipaddress
import getpass

input_server = input("Enter the IP of the server you'd like to connect to:")
login_name = input("Enter the username:")
login_pwd = getpass.getpass("Enter the password:")

#connect to ftp-server
ftp = FTP_TLS(input_server)
ftp.ssl_version
file_choice = input("""Enter the full path to the file including file extension of the file you'd like to upload.
Example:\"C:\\Users\\Andreas Stenberg\\Desktop\\FTP-skript.py\"n:""")
file = open(file_choice, "rb")
try:#Frågar efter server-IP och användarnamn och lösenord
    ftp.auth()
    ftp.login(login_name, login_pwd)
    print(ftp.getwelcome())
    ftp.prot_p()
    ftp.mlsd()
    ftp.storbinary("STOR {}".format(file_choice), file)
    time.sleep(5)
    ftp.quit()
    file.close()
except:
    ftp.quit()
