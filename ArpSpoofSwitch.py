# en 
# conf t
# int vlan 1
# ip address 192.168.122.XX 255.255.255.0
# no shut
# end
# username YassSSH password *********
# enable password *********
# line vty 0 4
# login local
# transport input all 
# end
# wr


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
tn.write(b"int range fa0/1-3\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 10\n")
tn.write(b"spanning-tree portfast\n")
tn.write(b"end\n")
tn.write(b"ip dhcp snooping\n")
tn.write(b"ip dhcp snooping vlan 10\n")
tn.write(b"no ip dhcp snooping information option\n")
tn.write(b"int fa0/3\n")
tn.write(b"ip dhcp snooping trust\n")
tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")
# ip arp inspection vlan 10

print(tn.read_all().decode('ascii'))