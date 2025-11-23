import socket

HOST = "127.0.0.1"
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Socket started", f"Host: {HOST}, Port: {PORT}")

conn, addres = server.accept()
print("Connecting, ", f"Adress: {addres}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break 
    print(data)
conn.close()