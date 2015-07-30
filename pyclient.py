import socket

addr = raw_input("Enter Address to send data to: ")
port = int(raw_input("Enter Port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((addr, port))

print "Hammer Time!"
while True:
    s.send('e' * 1024 * 1024)

