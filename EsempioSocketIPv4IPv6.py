# Programma server Echo
    import socket
    HOST = ’’
# Nome simbolico che rappresenta il nodo locale
    PORT = 50007
# Porta non privilegiata arbitraria
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print ’Connected by’, addr
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    conn.close()

# Programma client Echo
import socket
    HOST = ’daring.cwi.nl’
# Il nodo remoto
    PORT = 50007
# The La stessa porta usata dal server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(’Hello, world’)
    data = s.recv(1024)
    s.close()
    print ’Received’, ‘data‘

    # Programma server Echo
import socket
import sys
    HOST = ’’
# Nome simbolico che rappresenta il nodo locale
    PORT = 50007
# Porta non privilegiata arbitraria
    s = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI
        af, socktype, proto, canonname, sa = res
        try:
    s = socket.socket(af, socktype, proto)
        except socket.error, msg:
    s = None
    continue
        try:
    s.bind(sa)
    s.listen(1)
        except socket.error, msg:
    s.close()
    s = None
    continue
        break
    if s is None:
        print ’could not open socket’
        sys.exit(1)
    conn, addr = s.accept()
    print ’Connected by’, addr
    while 1:
        data = conn.recv(1024)
        if not data: break
            conn.send(data)
        conn.close()

# Programma client Echo
import socket
import sys
    HOST = ’daring.cwi.nl’
# Il nodo remoto
    PORT = 50007
# La stessa porta usata dal server
    s = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
    s = socket.socket(af, socktype, proto)
        except socket.error, msg:
    s = None
    continue
        try:
    s.connect(sa)
        except socket.error, msg:
    s.close()
    s = None
    continue
        break
    if s is None:
        print ’could not open socket’
        sys.exit(1)
    s.send(’Hello, world’)
    data = s.recv(1024)
    s.close()
    print ’Received’, ‘data‘
