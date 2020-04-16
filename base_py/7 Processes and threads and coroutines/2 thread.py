#__author__ = 'Winston'
#date: 2020/4/2

# 线程
# 在传统操作系统中，每个进程有一个地址空间，而且默认就有一个控制线程
#
# 线程顾名思义，就是一条流水线工作的过程，一条流水线必须属于一个车间，
# 一个车间的工作过程是一个进程
#
# 车间负责把资源整合到一起，是一个资源单位，而一个车间内至少有一个流水线
#
# 流水线的工作需要电源，电源就相当于cpu
#
# 所以，进程只是用来把资源集中到一起（进程只是一个资源单位，或者说资源集合），
# 而线程才是cpu上的执行单位。
#
# 多线程（即多个控制线程）的概念是，在一个进程中存在多个控制线程，
# 多个控制线程共享该进程的地址空间，相当于一个车间内有多条流水线，都共用一个车间的资源。
#
# 例如，北京地铁与上海地铁是不同的进程，而北京地铁里的13号线是一个线程，
# 北京地铁所有的线路共享北京地铁所有的资源，比如所有的乘客可以被所有线路拉。


# 线程的创建开销小
# 一个车间就是一个进程，一个车间至少一条流水线（一个进程至少一个线程）

# 创建一个进程，就是创建一个车间（申请空间，在该空间内建至少一条流水线）

# 而建线程，就只是在一个车间内造一条流水线，无需申请空间，所以创建开销小


# 进程之间是竞争关系，线程之间是协作关系
# 车间直接是竞争/抢电源的关系，竞争（不同的进程直接是竞争关系，是不同的程序员写的程序运行的，
# 迅雷抢占其他进程的网速，360把其他进程当做病毒干死）

# 一个车间的不同流水线式协同工作的关系（同一个进程的线程之间是合作关系，
# 是同一个程序写的程序内开启动，迅雷内的线程是合作关系，不会自己干自己）

# 线程与进程的区别
# 1）地址空间和其它资源（如打开文件）：进程间相互独立，同一进程的各线程间共享。某进程内的线程在其它进程不可见。
# 　　2）通信：进程间通信IPC，线程间可以直接读写进程数据段（如全局变量）来进行通信——需要进程同步和互斥手段的辅助，以保证数据的一致性。
# 　　3）调度和切换：线程上下文切换比进程上下文切换要快得多。
# 　　4）在多线程操作系统中，进程不是一个可执行的实体。


# 多线程
# 多线程指的是，在一个进程中开启多个线程，简单的讲：如果多个任务共用一块地址空间，那么必须在一个进程内开启多个线程。详细的讲分为4点：
#
# 多线程共享一个进程的地址空间
#
# 线程比进程更轻量级，线程比进程更容易创建可撤销，在许多操作系统中，创建一个线程比创建一个进程要快10-100倍，在有大量线程需要动态和快速修改时，这一特性很有用
#
# 若多个线程都是cpu密集型的(计算密集型)，那么并不能获得性能上的增强，但是如果存在大量的I/O处理，拥有多个线程允许这些活动彼此重叠运行，从而会加快程序执行的速度。
#
# 在多cpu系统中，为了最大限度的利用多核，可以开启多个线程，比开进程开销要小的多。（这一条并不适用于python）

# 开启线程的两种方式

# 方式一
from threading import Thread
import time

def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon',))
    t.start()
    print('主线程')

# 方式二
from threading import Thread
import time


class Sayhi(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)


if __name__ == '__main__':
    t = Sayhi('tony')
    t.start()
    print('主线程')

# 线程与进程
# pid的比较
from threading import Thread
from multiprocessing import Process
import os

def work():
    print('hello',os.getpid())

if __name__ == '__main__':
    #part1:在主进程下开启多个线程,每个线程都跟主进程的pid一样
    t1=Thread(target=work)
    t2=Thread(target=work)
    t1.start()
    t2.start()
    print('主线程/主进程pid',os.getpid())

    #part2:开多个进程,每个进程都有不同的pid
    p1=Process(target=work)
    p2=Process(target=work)
    p1.start()
    p2.start()
    print('主线程/主进程pid',os.getpid())

# 比较开启进程与线程的效率
from threading import Thread
from multiprocessing import Process
import os

def work():
    print('hello')

if __name__ == '__main__':
    #在主进程下开启线程
    t=Thread(target=work)
    t.start()
    print('主线程/主进程')
    '''
    打印结果:
    hello
    主线程/主进程
    '''

    #在主进程下开启子进程
    t=Process(target=work)
    t.start()
    print('主线程/主进程')
    '''
    打印结果:
    主线程/主进程
    hello
    '''

# 内存数据共享问题
from  threading import Thread
from multiprocessing import Process
import os
def work():
    global n
    n=0

if __name__ == '__main__':
    # n=100
    # p=Process(target=work)
    # p.start()
    # p.join()
    # print('主',n) #毫无疑问子进程p已经将自己的全局的n改成了0,但改的仅仅是它自己的,查看父进程的n仍然为100


    n=1
    t=Thread(target=work)
    t.start()
    t.join()
    print('主',n) #查看结果为0,因为同一进程内的线程之间共享进程内的数据

# 练习 ：多线程实现socket



# ----------------------------------------------------------------------------
#Thread实例对象的方法
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。

#threading模块提供的一些方法：
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。


from threading import Thread
import threading
from multiprocessing import Process
import os


def work():
    import time
    time.sleep(3)
    print(threading.current_thread().getName())


if __name__ == '__main__':
    # 在主进程下开启线程
    t = Thread(target=work)
    t.start()

    print(threading.current_thread().getName())
    print(threading.current_thread())  # 主线程
    print(threading.enumerate())  # 连同主线程在内有两个运行的线程
    print(threading.active_count())
    print('主线程/主进程')

    '''
    打印结果:
    MainThread
    <_MainThread(MainThread, started 140735268892672)>
    [<_MainThread(MainThread, started 140735268892672)>, <Thread(Thread-1, started 123145307557888)>]
    主线程/主进程
    Thread-1
    '''

# 主线程等待子线程结束
import time
def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('egon',))
    t.start()
    t.join()
    print('主线程')
    print(t.is_alive())
    '''
    egon say hello
    主线程
    False
    '''

# 守护线程
#无论是进程还是线程，都遵循：守护xx会等待主xx运行完毕后被销毁。需要强调的是：运行完毕并非终止运行

#1.对主进程来说，运行完毕指的是主进程代码运行完毕
#2.对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕

#1 主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收）,
# 然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束，

#2 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。
# 因为主线程的结束意味着进程的结束，
# 进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。

# 守护线程例1
from threading import Thread
import time
def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('egon',))
    t.setDaemon(True) #必须在t.start()之前设置
    t.start()

    print('主线程')
    print(t.is_alive())
    '''
    主线程
    True
    '''
# 守护线程例2
from threading import Thread
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")


t1=Thread(target=foo)
t2=Thread(target=bar)

t1.daemon=True
t1.start()
t2.start()
print("main-------")

# 死锁现象与递归锁
# 进程也有死锁与递归锁，在进程那里忘记说了，放到这里一切说了额
#
# 所谓死锁： 是指两个或两个以上的进程或线程在执行过程中，
# 因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。
# 此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程，
# 如下就是死锁

# 死锁示例
from threading import Thread,Lock
import time
mutexA=Lock()
mutexB=Lock()

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()
    def func1(self):
        mutexA.acquire()
        print('\033[41m%s 拿到A锁\033[0m' %self.name)

        mutexB.acquire()
        print('\033[42m%s 拿到B锁\033[0m' %self.name)
        mutexB.release()

        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[43m%s 拿到B锁\033[0m' %self.name)
        time.sleep(2)

        mutexA.acquire()
        print('\033[44m%s 拿到A锁\033[0m' %self.name)
        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t=MyThread()
        t.start()

'''
Thread-1 拿到A锁
Thread-1 拿到B锁
Thread-1 拿到B锁
Thread-2 拿到A锁
然后就卡住，死锁了
'''

# 解决方法，递归锁，在Python中为了支持在同一线程中多次请求同一资源，
# python提供了可重入锁RLock。
#
# 这个RLock内部维护着一个Lock和一个counter变量，
# counter记录了acquire的次数，从而使得资源可以被多次require。
# 直到一个线程所有的acquire都被release，其他的线程才能获得资源。
# 上面的例子如果使用RLock代替Lock，则不会发生死锁：

# mutexA=mutexB=threading.RLock() #一个线程拿到锁，counter加1,
# 该线程内又碰到加锁的情况，则counter继续加1，这期间所有其他线程都只能等待，等待该线程释放

# 递归锁RLock
from threading import RLock as Lock
import time
mutexA=Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()


# 典型问题：科学家吃面
# 死锁问题
import time
from threading import Thread,Lock
noodle_lock = Lock()
fork_lock = Lock()
def eat1(name):
    noodle_lock.acquire()
    print('%s 抢到了面条'%name)
    fork_lock.acquire()
    print('%s 抢到了叉子'%name)
    print('%s 吃面'%name)
    fork_lock.release()
    noodle_lock.release()

def eat2(name):
    fork_lock.acquire()
    print('%s 抢到了叉子' % name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s 抢到了面条' % name)
    print('%s 吃面' % name)
    noodle_lock.release()
    fork_lock.release()

for name in ['哪吒','egon','yuan']:
    t1 = Thread(target=eat1,args=(name,))
    t2 = Thread(target=eat2,args=(name,))
    t1.start()
    t2.start()

# 递归锁解决
import time
from threading import Thread,RLock

fork_lock = noodle_lock = RLock()
def eat1(name):
    noodle_lock.acquire()
    print('%s 抢到了面条'%name)
    fork_lock.acquire()
    print('%s 抢到了叉子'%name)
    print('%s 吃面'%name)
    fork_lock.release()
    noodle_lock.release()

def eat2(name):
    fork_lock.acquire()
    print('%s 抢到了叉子' % name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s 抢到了面条' % name)
    print('%s 吃面' % name)
    noodle_lock.release()
    fork_lock.release()

for name in ['哪吒','egon','yuan']:
    t1 = Thread(target=eat1,args=(name,))
    t2 = Thread(target=eat2,args=(name,))
    t1.start()
    t2.start()

# 信号量Semaphore
# 同进程的一样
#
# Semaphore管理一个内置的计数器，
# 每当调用acquire()时内置计数器-1；
# 调用release() 时内置计数器+1；
# 计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
#
# 实例：(同时只有5个线程可以获得semaphore,即可以限制最大连接数为5)：
from threading import Thread,Semaphore
import threading
import time
# def func():
#     if sm.acquire():
#         print (threading.currentThread().getName() + ' get semaphore')
#         time.sleep(2)
#         sm.release()
def func():
    sm.acquire()
    print('%s get sm' %threading.current_thread().getName())
    time.sleep(3)
    sm.release()
if __name__ == '__main__':
    sm=Semaphore(5)
    for i in range(23):
        t=Thread(target=func)
        t.start()

# 与进程池是完全不同的概念，进程池Pool(4)，最大只能产生4个进程，
# 而且从头到尾都只是这四个进程，不会产生新的，而信号量是产生一堆线程/进程

# Event
# 同进程的一样
#
# 线程的一个关键特性是每个线程都是独立运行且状态不可预测。
# 如果程序中的其 他线程需要通过判断某个线程的状态来确定自己下一步的操作,
# 这时线程同步问题就会变得非常棘手。为了解决这些问题,
# 我们需要使用threading库中的Event对象。 对象包含一个可由线程设置的信号标志,
# 它允许线程等待某些事件的发生。在 初始情况下,Event对象中的信号标志被设置为假。
# 如果有线程等待一个Event对象, 而这个Event对象的标志为假,
# 那么这个线程将会被一直阻塞直至该标志为真。一个线程如果将一个Event对象的信号标志设置为真,
# 它将唤醒所有等待这个Event对象的线程。如果一个线程等待一个已经被设置为真的Event对象,
# 那么它将忽略这个事件, 继续执行

# event.isSet()：返回event的状态值；
# event.wait()：如果 event.isSet()==False将阻塞线程；
# event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
# event.clear()：恢复event的状态值为False。


# 有多个工作线程尝试链接MySQL，我们想要在链接前确保MySQL服务正常才让
# 那些工作线程去连接MySQL服务器，如果连接不成功，都会去尝试重新连接。
# 那么我们就可以采用threading.Event机制来协调各个工作线程的连接操作

from threading import Thread,Event
import threading
import time,random
def conn_mysql():
    count=1
    while not event.is_set():
        if count > 3:
            raise TimeoutError('链接超时')
        print('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
        event.wait(0.5)
        count+=1
    print('<%s>链接成功' %threading.current_thread().getName())


def check_mysql():
    print('\033[45m[%s]正在检查mysql\033[0m' % threading.current_thread().getName())
    time.sleep(random.randint(2,4))
    event.set()
if __name__ == '__main__':
    event=Event()
    conn1=Thread(target=conn_mysql)
    conn2=Thread(target=conn_mysql)
    check=Thread(target=check_mysql)

    conn1.start()
    conn2.start()
    check.start()



# GIL全局解释锁
'''
定义：
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple 
native threads from executing Python bytecodes at once. This lock is necessary mainly 
because CPython’s memory management is not thread-safe. (However, since the GIL 
exists, other features have grown to depend on the guarantees that it enforces.)
'''
# 结论：在Cpython解释器中，同一个进程下开启的多线程，同一时刻只能有一个线程执行，无法利用多核优势

# GIL并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念。
# 就好比C++是一套语言（语法）标准，但是可以用不同的编译器来编译成可执行代码。
# 有名的编译器例如GCC，INTEL C++，Visual C++等。Python也一样，
# 同样一段代码可以通过CPython，PyPy，Psyco等不同的Python执行环境来执行。
# 像其中的JPython就没有GIL。

# GIL本质就是一把互斥锁，既然是互斥锁，所有互斥锁的本质都一样，
# 都是将并发运行变成串行，以此来控制同一时间内共享数据只能被一个任务所修改，
# 进而保证数据安全。

# 解释器的代码是所有线程共享的，所以垃圾回收线程也可能访问到解释器的代码而去执行，
# 这就导致了一个问题:对于同一个数据100，可能线程1执行x=100的同时，
# 而垃圾回收执行的是回收100的操作，解决这种问题没有什么高明的方法，
# 就是加锁处理，如下图的GIL，保证python解释器同一时间只能执行一个任务的代码

# GIL保护的是解释器级的数据，保护用户自己的数据则需要自己加锁处理

# 有了GIL的存在，同一时刻同一进程中只有一个线程被执行

# 进程可以利用多核，但是开销大，而python的多线程开销小，
# 但却无法利用多核优势，也就是说python没用了？

#1. cpu到底是用来做计算的，还是用来做I/O的？
#2. 多cpu，意味着可以有多个核并行完成计算，所以多核提升的是计算性能
#3. 每个cpu一旦遇到I/O阻塞，仍然需要等待，所以多核对I/O操作没什么用处


# 分析：
# 我们有四个任务需要处理，处理方式肯定是要玩出并发的效果，解决方案可以是：
# 方案一：开启四个进程
# 方案二：一个进程下，开启四个线程

# 单核情况下，分析结果:
# 　　如果四个任务是计算密集型，没有多核来并行计算，方案一徒增了创建进程的开销，方案二胜
# 　　如果四个任务是I / O密集型，方案一创建进程的开销大，且进程的切换速度远不如线程，方案二胜
#
# 多核情况下，分析结果：
# 　　如果四个任务是计算密集型，多核意味着并行计算，在python中一个进程中同一时刻只有一个线程执行用不上多核，方案一胜
# 　　如果四个任务是I / O密集型，再多的核也解决不了I / O问题，方案二胜

# 结论：现在的计算机基本上都是多核，python对于计算密集型的任务开多线程的效率并不能带来多大性能上的提升，甚至不如串行(没有大量切换)，但是，对于IO密集型的任


# 多线程性能测试

# 计算密集型:多进程效率高
# I/O密集型:多线程效率高

#多线程用于IO密集型，如socket，爬虫，web
#多进程用于计算密集型，如金融分析