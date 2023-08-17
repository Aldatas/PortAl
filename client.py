import socket


def Main():
    print("Host IP: ")
    host = input()
    print("Port: ")
    port = int(input())

    # Config
    # host = '' #Server ip
    # port = 4000
    
    server = (host, port)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    
    message = input("-> ")
    while message !='q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)
        message = input("-> ")
    s.close()

if __name__=='__main__':
    Main()