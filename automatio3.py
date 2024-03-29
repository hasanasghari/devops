import telnetlib 
import getpass
user = input("Enter your Username: ")
password = getpass.getpass()
Host=["192.168.122.100","192.168.122.200"] # List of the routers and switches.
Port=9023 # Port number
Connection=telnetlib.Telnet(Host[0]) # OOP of telnetlib  telnetlib.Telnet(host=None, port=0[, timeout])
print(Connection.get_socket()) # find socket address
Connection.read_until(b"Username: ") #Telnet.read_until(expected, timeout=None)
Connection.write(user.encode('ascii') + b"\n")
if password:
    Connection.read_until(b"Password: ")
    Connection.write(password.encode("ascii") + b"\n")


Connection.write(b"show vlan brief\n")
Connection.write(b"exit\n")

print(Connection.read_all().decode('ascii'))

