import socket
import threading

IP = '192.168.1.64'
PORT = 6969

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.connect((IP, PORT))


def receive_messages():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode('utf-8'))
        except Exception as e:
            print("Error receiving message:", e)
            break


def send_messages():
    while True:
        message = input("")
        if message.strip().lower() == "/disconnect":
            client.send(message.encode('utf-8'))
            print("You have been disconnected.")
            break
        else:
            client.send(message.encode('utf-8'))


threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
