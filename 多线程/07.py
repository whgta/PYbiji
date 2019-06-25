import time
import threading
def fun():
    print('Sta fun')
    time.sleep(2)
    print('end fun')

print('Main thread')

t1 = threading.Thread(target=fun,args=())
# 设成守护线程的方法，必须在start之前设置，否则无效
t1.setDaemon(True)
t1.start()
time.sleep(1)
print('Main thread end')