import socket
import sys

# create socket to iniciate communication


def create_socket():
    try:
        global host
        global port
        global sock
        host = ""
        port = 9999
        sock = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# bind socket with the host
# in pyhton when you want to access the global variable then you have to declear them all over again


def bind_socket():
    try:
        global host
        global port
        global sock
        print("Binding the port " + str(port) + " ......")
        sock.bind((host, port))  # as this is a tuple we used two pair of prentecies here
        sock.listen(5)
    except socket.error as msg:
        print("Socket Binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Accept the connection/ Establish the connection


def socket_accept():
    connection, ip_address = sock.accept()
    print("Connection has been established! " + "\nIP: " + ip_address[0] + " | Port: " + str(ip_address[1]))
    send_messeges(connection)
    connection.close()


def send_messeges(connection):
    while True:
        msges = input("Now you can send messages: ")
        connection.send(str.encode(msges))
        client_response = str(connection.recv(1024), "utf-8")
        print(client_response, end=" ")

        if msges == "Quit":
            connection.close()


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
