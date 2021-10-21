# en 
# conf t
# int fa0/0
# ip address 192.168.122.XX 255.255.255.0
# no shut
# username YassSSH password *********
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
tn.write(b"int fa0/0\n")
tn.write(b"ip dhcp pool POOL_IRIS\n")
tn.write(b"network 192.168.1.0 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))