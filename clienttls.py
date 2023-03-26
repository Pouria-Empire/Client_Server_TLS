import os
from socket import create_connection,socket,AF_INET,SOCK_DGRAM
from ssl import SSLContext, PROTOCOL_TLS_CLIENT
#import sslkeylog

ip = '127.0.0.1'
port = 8442

def senMessage(message,server_ip,server_port):
    #sslkeylog.set_keylog(os.environ.get('SSLKEYLOGFILE'))
    hostname='localhost'
    ip = server_ip
    port = server_port
    context = SSLContext(PROTOCOL_TLS_CLIENT) #initializing tls connection
    context.load_verify_locations('./new.pem')  #verifing

    with create_connection((ip, port)) as client:
        with context.wrap_socket(client, server_hostname=hostname) as tls:
            print(f'Using {tls.version()}\n')
            tls.sendall(message.encode('ascii'))    # send message

            data = tls.recv(1024)   #recieve reply from server
            print(f'Server says: {data}')   

if __name__ == "__main__":
    senMessage("Hi to Server from Client",ip,port)

    n = input("press any key to exit...")