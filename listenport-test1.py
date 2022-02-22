# client example

# python plug-ins to load
import socket, time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host and port to listen on
client_socket.connect(('localhost', 3389))
while True:
    time.sleep(5)
    data = client_socket.recv(512)
    if data.lower() == 'q':
        client_socket.close()
        break

    print("RECEIVED: %s" % data)
    data = input("SEND( TYPE q or Q to Quit):")
    client_socket.send(data)
    if data.lower() == 'q':
        client_socket.close()
        break