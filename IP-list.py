import os
import random


iplist = []
xrange = range(1,1000)


for i in xrange:

  ip = "10."

  ip += ".".join(map(str, (random.randint(0, 255)
                          for i in range(3))))
  iplist.append(ip)
#Sparar IP-adresserna i en lista som heter iplist.
with open("IP-list.txt", 'w') as listfil:
    for ip_address in iplist:
        listfil.write("{}\n".format(ip_address))
listfil.close
