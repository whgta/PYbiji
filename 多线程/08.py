import time
import threading
def loop1():
    # ctime 得到当前时间
    print('S loop 1 at: ',time.ctime())
    # 睡眠多长时间，单位秒
    time.sleep(4)
    print('E loop 1 at :',time.ctime())

def loop2():
    # ctime 得到当前时间
    print('S loop 2 at: ',time.ctime())
    # 睡眠多长时间，单位秒
    time.sleep(2)
    print('E loop 2 at :',time.ctime())

def loop3():
    # ctime 得到当前时间
    print('S loop 3 at: ',time.ctime())
    # 睡眠多长时间，单位秒
    time.sleep(5)
    print('E loop 3 at :',time.ctime())

def main():
    print('S at: ',time.ctime())
    t1 = threading.Thread(target=loop1,args=())
    t1.setName('THR_1')
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName('THR_2')
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName('THR_3')
    t3.start()
    # 预期3秒后，thread2已经自动结束
    time.sleep(3)
    # enumerate 得到正在运行的子程序，即子线程1和子线程3
    for thr in threading.enumerate():
        print("正在运行的线程名字：{0}".format(thr.getName()))
    print("正在运行的子线程数量为：{0}".format(threading.activeCount()))

    print("ALL done",time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)