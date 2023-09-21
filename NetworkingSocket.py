import socket
#the parameters specify that the socket will be able to across the internet
                                        #string of charater that came one after other
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                #name of the host to make the call    
mysock.connect('google.com',80)
                                #port

