import socket

def tcp_clt():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接对方，请求根对方建立通路
    addr = ("127.0.0.1", 8998)
    sock.connect(addr)
    # 3.发送内容到对方服务器
    msg = "i love wanghao "
    sock.send(msg.encode())
    rst = sock.recv(500)
    print(rst.decode())

    sock.close()

if __name__ == '__main__':
    tcp_clt()