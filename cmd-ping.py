import subprocess
import ipaddress

net_addr = input("Enter a network address")

ip_net = ipaddress.ip_network(net_addr)

all_hosts = list(ip_net.hosts())


for i in range(len(all_hosts)):
  output = subprocess.Popen(['ping', '-n', '1,' '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]


  if "Destination host unreachable" in output.decode('utf-8'):
       print(str(all_hosts[i]), "is Offline")
   elif "Request timed out" in output.decode('utf-8'):
       print(str(all_hosts[i]), "is Offline")
   else:
       print(str(all_hosts[i]), "is Online")
