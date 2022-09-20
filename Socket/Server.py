#####################################################################
#   Server.py
#       - This shows how to use server by using python
#           . description
#   written by jslee
#   date : 2000.00.00
#####################################################################


import socket 



class pScoket():
    def __init__(self, ip, port):
       print(f'socket init..\n')
       self.ip = ip
       self.port = port 
    
    
    ###################################################
    # client
    ###################################################
    
    # create IPv4, tcp client socket 
    def tcp_client_socket(self):
        
        # create client socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'create IPv4 tcp client socket\n')
        
        # connect
        self.sock.connect((self.ip, self.port))
        print(f'connnect : {self.ip}, {self.port}')

        return self.sock
    
    
    # create IPv4, udp socket 
    def udp_client_socket(self):
        pass

    
    # close client socket
    def tcp_client_close(self):
        self.sock.close()



    ###################################################
    # server
    ###################################################
    
    # create IPv4, tcp server socket 
    def tcp_server_socket(self):
        
        # create server socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'create IPv4 tcp server socket\n')
        
        # set server socket 
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
    def udp_server_socket(self):
        pass

    
    # close server socket
    def close_socket(self):
        self.client_socket.close()
        self.sock.close()
        
        

ip = '127.0.0.1'
port = 9999


if __name__ == '__main__':
    
    server = pScoket(ip, port)
    
    # tcp socket
    client_sock, addr = server.tcp_server_socket()
    
    
    # data send & recv 부분 update 필요...
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        print('receive data ', addr, data.decode())
    
    
    
    print(f'Done..')