import socket
import threading

IP = '192.168.1.74'
PORT = 6969

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.bind(('0.0.0.0', 0))
print(f"Client running on {client.getsockname()}")

client.settimeout(5)

server_address = (IP, PORT)
connected = False


def receive_messages():
    while True:
        try:
            message, addr = client.recvfrom(1024)
            print(message.decode('utf-8'))

        except socket.timeout:
            continue
        except Exception as e:
            print("Error receiving message:", e)
            break


def send_messages():
    global connected
    while True:
        message = input("")
        if message.strip().lower() == "/connect":
            client.connect(server_address)
            print("Connected to server.")
            connected = True
            client.send("/connect".encode('utf-8'))
        elif message.strip().lower() == "/disconnect":
            connected = False
            client.send("/disconnect".encode('utf-8'))
            print("You have been disconnected.")
        elif connected:
            client.send(message.encode('utf-8'))
        else:
            print("You must connect first using /connect")


threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
