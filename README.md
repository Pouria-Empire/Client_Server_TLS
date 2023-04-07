# Client_Server_TLS
A client server tls app

# Explaining how does it works
## linux send udp request
echo -n "say: some data..., to: 5555" | nc -4u -w0 127.0.0.1 8081

## linux udp listen on specific port
netcat -ul 8081


## Commands to run in OpenSSL:
1. openssl genrsa -aes256 -out private.key 2048
2. openssl rsa -in private.key -out private.key
3. openssl req -new -x509 -nodes -sha1 -key private.key -out certificate.crt -days 36500
4. openssl req -x509 -new -nodes -key private.key -sha1 -days 36500 -out new.pem

## Messages :
## app on client with udp sending below message to xclient:
say: "some data...", to: $IP:$PORT

# Usage in Linux
first run servertls.py, then run clienttls.py
```bash
python3 <SCRIPT >.py
```
