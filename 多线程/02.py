'''
l利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''

import time
import _thread as thread
def loop1():
    # ctime 得到当前时间
    print('S loop 1 at: ',time.ctime())
    # 睡眠多长时间，单位秒
    time.sleep(4)
    print('E loop 1 at :',time.ctime())


def loop2():
    # ctime 得到当前时间
    print('S loop 2 at: ', time.ctime())
    # 睡眠多长时间，单位秒
    time.sleep(2)
    print('E loop 2 at :', time.ctime())

def main():
    print('S at: ',time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数两个，一个是需要运行的参数名，第二个是函数的参数作为元组使用，为空则使用空远足
    # 注意：如果函数只有一个参数，需要参数由后一个逗号
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2, ())
    print('all done at: ',time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)