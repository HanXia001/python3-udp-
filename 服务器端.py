import socket

dest = ("192.168.77.255",1060)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

s.sendto("Hi".encode("utf-8"),dest)
print("等待对方回复（按ctrl+c退出）")
while True:
    (buf,address) = s.recvfrom(2048)
    print("Received from %s : %s"%(address,buf))

