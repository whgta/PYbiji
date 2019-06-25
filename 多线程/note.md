# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python3.7
- https://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 vs 多进程
- 程序：一堆代码以文本形似存入一个文档
- 进程：程序运行的一个状态
    - 包含地址空间，内存，数据摘等
    - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁（GIL）
    - Python代码的执行是由python虚拟机进行控制
    - 在主循环中只能更有一个控制线程在执行
- python包
    - thread：有问题，不好用，python3中_thread
    - threading：通行的包
    - 案例01：顺序执行，耗时比较长
    - 案例02：改用多线程，缩短总时间，使用_thread
    
- threading的使用
    - 直接利用threading，Thread生成Thread实例
        1. t = threading.Thread(target=xxx,args=(xxx,))
        2. t.start():启动多线程
        3. t,join():等待多线程执行完成
        4. 案例04  
        5. 加入join与案例04相比较，案例05 
        - 守护线程-daemon
            - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
            - 一般认为，守护线程不重要或者不允许离开主线程独立运行
            - 守护线程案例能否有效果跟环境相关
            - 案例06非守护线程
            - 案例07守护线程
        - 线程常用属性 
            - threading.currentThread:返回当前线程变量
            - threading.enumerate:返回一个包含正在运行的线程list，正在运行的线程指的是线程启动后，结束前
            - threading.activeCount:返回正在运行的线程数量，效果跟len(threading.enumerate)相同
            - threading.setName:给线程设置名称
            - threading.getName：得到线程的名字
- 共享变量
    - 共享变量;当多个线程同时范围跟一个变量的时候，会产生共享问题
    - 案例11
    - 解决变量：锁，信号灯
    - 锁（Lock）：
        - 是一个标志，表示一个线程在占用一些资源
        - 使用方法
            - 上锁
            - 使用共享资源，放心的用
            - 取消锁，解放锁
        - 案例12
        - 锁谁：哪个资源需要多个线程共享，锁哪个
        - 理解锁：锁其实不是锁谁，而是一个令牌
    - 线程安全问题：
        - 如果一个资源/变量，他对于多线程来讲，不用枷锁也不会引起任何问题，则称为线程安全
        - 线程不安全变量类型：list，set，dict
        - 安全变量：queue
    - 生产者消费者问题
        - 一个模型，可以用来搭建消息队列
        - queue是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list
    - 死锁问题案例14
    - 锁的等待时间问题 v15
    - semphore
        - 允许一个资源最多由几个多线程同时使用
        - v16
    - threading.Timer
        - 案例17
        - Timer是利用多线程，在指定时间启动一个功能
        
    - 可重入锁
        - 一个锁，可以被一个线程多次申请
        - 主要解决递归调用的时候，需要申请锁的情况
        - 案例18
        
# 线程替代方案
- subprocess
    - 完全跳过线程，使用进程
    - 是派生进程的主要代替方案
- multiprocessiong
    - 使用threading接口派生，使用子进程
    - 允许为多喝或者多cpu派生进程，接口跟threading非常相似
    
- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    
# 多进程
- 进程间通讯（IPC）
- 进程之间无任何共享状态
- 进程的创建
    - 案例19
       

                

           
            
    