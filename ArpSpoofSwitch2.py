import getpass
import telnetlib

HOST = "192.168.122.XX"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"test\n")
tn.write(b"conf t\n")
tn.write(b"arp access-list DHCP_ROUTER\n")
tn.write(b"permit ip host 192.168.1.254 mac host #METTRE LA MAC DU ROUTEUR DHCP\n")
tn.write(b"ip arp inspection filter DHCP_ROUTER vlan 10\n")
tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")
# ip arp inspection vlan 10

print(tn.read_all().decode('ascii'))