from socket import socket, AF_INET, SOCK_STREAM,SOCK_DGRAM
from ssl import SSLContext, PROTOCOL_TLS_SERVER
import _thread as thread
from concurrent.futures import ThreadPoolExecutor
import random # define the random module  
import string  
S = 10  # number of characters in the string.


MAX_DATA_RECV = 4096

ip = '127.0.0.1'
port = 8442
context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain('./new.pem', './private.key') #load tls connection

def func_thread(data, connection):
    global ip,port,context

    print(f'Client Says: {data}')
    
    # recieve response and print it

    ran = "The Flag is : " + str(''.join(random.choices(string.ascii_uppercase + string.digits, k = S)))  
    recv_data = ran.encode('ascii')

    # send back response
    connection.sendall(recv_data) 


    print(f"response: {recv_data} sent")


def runTLSServer(server_listen_ip,server_listen_port):
    executor = ThreadPoolExecutor(max_workers=4)
    global ip,port,context
    ip = server_listen_ip
    port = server_listen_port
    #create socket and listening on

    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind((ip, port))
        server.listen(1)

        with context.wrap_socket(server, server_side=True) as tls:
            while 1:
                connection, address = tls.accept()  # waiting for connection
                print(f'Connected by {address}\n')

                data = connection.recv(1024) #recieve data

                executor.submit(func_thread, data, connection)

              
if __name__ == "__main__":
     runTLSServer(ip,port)