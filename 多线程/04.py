import time
import threading
def loop1(in1):
    # ctime 得到当前时间
    print('S loop 1 at: ',time.ctime())
    # 把参数打印出俩
    print('我是参数：',in1)
    # 睡眠多长时间，单位秒
    time.sleep(4)
    print('E loop 1 at :',time.ctime())


def loop2(in1,in2):
    # ctime 得到当前时间
    print('S loop 2 at: ', time.ctime())
    print('我是参数',in1,'和参数：',in2)
    # 睡眠多长时间，单位秒
    time.sleep(2)
    print('E loop 2 at :', time.ctime())

def main():
    print('S at: ',time.ctime())
    t1 = threading.Thread(target=loop1,args=('王大哥',))
    t1.start()
    t2 = threading.Thread(target=loop2, args=('王大哥','王晓鹏'))
    t2.start()
    print('all done at: ',time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)