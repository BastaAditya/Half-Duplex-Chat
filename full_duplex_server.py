from socket import*
import threading
import time

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('...waiting for connection')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from',addr)

    def receive():
        global tcpCliSock
        while True:
            time.sleep(1)
            mssg_c = tcpCliSock.recv(BUFSIZ)
            print("Client : ",end="")
            print(mssg_c.decode('utf-8'))
            if mssg_c.decode('utf-8') == "Bye":
                break


    def send():
        global tcpCliSock
        while True:
            time.sleep(1)
            mssg_s = input("You : ")
            tcpCliSock.send(mssg_s.encode())
            if mssg_s == "Bye":
                break

    while True:
        t1 = threading.Thread(target = receive)
        t2 = threading.Thread(target = send)

        t1.start()
        t2.start()

        t1.join()
        t2.join()
        break
        
    tcpCliSock.close()
tcpSerSock.close()
        
