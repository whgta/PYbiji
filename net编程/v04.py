import socket


def tcp_srv():
    # 1.建立socket负责具体通信，只负责接受对方的请求，真正的通信时链接后
    # 需要用到两个参数
    # SOCK_STREAM：表明使用tcp进行通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定端口和地址
    addr = ("127.0.0.1",8998)
    sock.bind(addr)
    # 3.监听接入的访问socket
    sock.listen()

    while True:
        # 4.接受访问的socket，可以理解接受范围跟即建立了一个通信的连接通路
        #accept返回的元组第一个元素赋值给sjt，第二个赋值给addr
        skt,addr = sock.accept()
        # 5. 接受对方的发送内容，利用接受到的socket接受内容
        # 500代表接受使用的buffersize
        # msg = skt,receive(500)
        msg = skt.recv(500)
        # 接受到的时bytes格式内容
        # 想得到str格式，解码
        msg = msg.decode()

        rst = "REcived msg:{0} from {1}".format(msg.addr)
        print(rst)
        # 6.回馈
        skt.send(rst.encode())

        #7.关闭链路
        skt.close()


if __name__ == '__main__':
    print("STarting server...........")
    tcp_srv()
    print("Ending server............")