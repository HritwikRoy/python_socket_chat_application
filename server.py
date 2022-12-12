import socket
import threading
import time

my_port=12372
my_ip_address="127.0.0.1"

client_port=32172
client_ip_address="127.0.0.1"

# created my and cliend socket

s=socket.socket()
sd=socket.socket()

# my socked

s.bind((my_ip_address,my_port))
s.listen(10)
c,addr=s.accept()



# cliend socket connect

sd.connect((client_ip_address,client_port))




while True:

# input SMS....

    def input_sms():
        sms = input("")
        if sms:
            c.send(sms.encode())
            if (sms=="exit"):
                exit() # break


    #input_sms()

# recv SMS.....
    def recv_sms():
        recv_sms=sd.recv(client_port).decode()
        if(recv_sms=="exit"):
            exit()
        else:
            print(f"{recv_sms}")

    #recv_sms()

    t1=threading.Thread(target=input_sms)
    t2=threading.Thread(target=recv_sms)

    


    t2.start()
    t1.start()
    time.sleep(0.1)
#    t1.join()


s.close()
sd.close()