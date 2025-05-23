import socket

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
    print("Connected!")
except Exception as e:
    print(f"Connection failed: {e}")
