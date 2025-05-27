# server.py

import socket
import threading
import logging

logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

IP = '0.0.0.0'
PORT = 6969

connected_clients = set()

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((IP, PORT))
logging.info(f"Server started on {IP}:{PORT}")
print(f"Server started on {IP}:{PORT}")


def broadcast(message, sender_addr):
    print(f"Broadcasting: {message.decode('utf-8')}")
    for client_addr in connected_clients:
        if client_addr != sender_addr:
            try:
                server.sendto(message, client_addr)
            except Exception as e:
                logging.error(f"Failed to send to {client_addr}: {e}")


def listen():
    while True:
        try:
            message, addr = server.recvfrom(1024)
            decoded_message = message.decode('utf-8').strip()
            if addr in connected_clients:
                logging.info(f"Received from {addr}: {decoded_message}")
            else:
                logging.warning(f"Unauthorized message from {addr}: {decoded_message}")

            if decoded_message.lower() == "/connect":
                if addr not in connected_clients:
                    connected_clients.add(addr)
                    logging.info(f"Client {addr} connected.")
                    server.sendto(b"Connected to server successfully!", addr)
                else:
                    server.sendto(b"You're already connected.", addr)
                continue

            if decoded_message.lower() == "/disconnect":
                if addr in connected_clients:
                    connected_clients.remove(addr)
                    logging.info(f"Client {addr} disconnected.")
                    server.sendto(b"Disconnected successfully.", addr)
                else:
                    server.sendto(b"You were not connected.", addr)
                continue

            if addr in connected_clients:
                broadcast(message, addr)
            else:
                server.sendto(b"Please connect first using /connect", addr)
                continue

        except Exception as e:
            logging.error(f"Error receiving message: {e}")


listen_thread = threading.Thread(target=listen)
listen_thread.start()
