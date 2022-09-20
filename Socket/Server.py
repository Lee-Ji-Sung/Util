#####################################################################
#   Server.py
#       - This shows how to use server by using python
#           . description
#   written by jslee
#   date : 2000.00.00
#####################################################################


import socket 



class Server():
    def __init__(self, ip, port):
       print(f'server init..\n')
       self.ip = ip
       self.port = port 
    
    # create IPv4, tcp socket 
    def tcp_socket(self):
        
        # create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'create IPv4 tcp server socket\n')
        
        # set socket 
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    #### --> to study..
        
        # bind
        self.sock.bind((self.ip, self.port))
        print(f'tcp server bind...\n')
        
        # listen
        self.sock.listen()
        print(f'tcp server listen...\n')
        
        # accept 
        self.client_socket, addr = self.sock.accept()
        print(f'Connected ip : {addr}\n')
        
        return self.client_socket, addr
    
    
    # create IPv4, udp socket 
    def udp_socket(self):
        pass

    
    # close socket
    def close_socket(self):
        self.client_socket.close()
        self.sock.close()
        
        

ip = '127.0.0.1'
port = 9999


if __name__ == '__main__':
    
    server = Server(ip, port)
    
    # tcp socket
    client_sock, addr = server.tcp_socket()
    
    while True:
        data = client_sock.recv(1024)

        print('receive data ', addr, data.decode())
    
    
    
    print(f'Done..')