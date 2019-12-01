import getpass
import sys
import telnetlib
import time

HOST = "10.110.10.1"
PORT=9023
user = raw_input("Enter your Telnet Username: ")
password = getpass.getpass()


command_1='ip address print'
command_3='quit'


tn = telnetlib.Telnet(HOST,PORT)
#input user
tn.read_until(b"Login: ")
tn.write(user.encode('UTF-8') + b"\n")
#input password
tn.read_until(b"Password: ")
tn.write(password.encode('UTF-8') + b"\n")

tn.read_until(b'>')
tn.write(command_1.encode('UTF-8')+b"\r\n")
time.sleep(5)
tn.read_until(b'>')
tn.write(command_3.encode('UTF-8')+b"\r\n")

print tn.read_all()
tn.close()
