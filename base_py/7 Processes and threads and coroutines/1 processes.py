#__author__ = 'Winston'
#date: 2020/4/2

# 进程

# 进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，
# 是系统进行资源分配和调度的基本单位，是操作系统结构的基础。
# 在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；
# 在当代面向线程设计的计算机结构中，进程是线程的容器。
# 程序是指令、数据及其组织形式的描述，进程是程序的实体。
#
# 狭义定义：进程是正在运行的程序的实例
# （an instance of a computer program that is being executed）。

# 广义定义：进程是一个具有一定独立功能的程序关于某个数据集合的一次运行活动。
# 它是操作系统动态执行的基本单元，在传统的操作系统中，进程既是基本的分配单元，
# 也是基本的执行单元。

# 进程与程序的区别
# 程序是指令和数据的有序集合，其本身没有任何运行的含义，是一个静态的概念。
# 而进程是程序在处理机上的一次执行过程，它是一个动态的概念。
# 程序可以作为一种软件资料长期存在，而进程是有一定生命期的。
# 程序是永久的，进程是暂时的。

# 注意：同一个程序执行两次，就会在操作系统中出现两个进程，
# 所以我们可以同时运行一个软件，分别做不同的事情也不会混乱。


# 进程调度
# 要想多个进程交替运行，操作系统必须对这些进程进行调度，
# 这个调度也不是随即进行的，而是需要遵循一定的法则，由此就有了进程的调度算法。


# 进程的并行与并发

# 并行 : 并行是指两者同时执行，比如赛跑，两个人都在不停的往前跑；
# （资源够用，比如八个线程，四核的CPU ）

# 并发 : 并发是指资源有限的情况下，两者交替轮流使用资源，
# 比如一段路(单核CPU资源)同时只能过一个人，A走一段后，
# 让给B，B用完继续给A ，交替使用，目的是提高效率。

# 区别:
# 并行是从微观上，也就是在一个精确的时间片刻，有不同的程序在执行，这就要求必须有多个处理器。
# 并发是从宏观上，在一个时间段上可以看出是同时执行的，比如一个服务器同时处理多个session。
#单个cpu+多道技术就可以实现并发,(并行也属于并发)

# 多道技术概念回顾：内存中同时存入多道（多个）程序，
# cpu从一个进程快速切换到另外一个，使每个进程各自运行几十或几百毫秒，
# 这样，虽然在某一个瞬间，一个cpu只能执行一个任务，但在1秒内，
# cpu却可以运行多个进程，这就给人产生了并行的错觉，即伪并发，
# 以此来区分多处理器操作系统的真正硬件并行（多个cpu共享同一个物理内存）


# 同步异步阻塞非阻塞

# 进程的几个状态。在程序运行的过程中，由于被操作系统的调度算法控制，
# 程序会进入几个状态：就绪，运行和阻塞。
#
# 一、就绪(Ready)状态
# 当进程已分配到除CPU以外的所有必要的资源，只要获得处理机便可立即执行，
# 这时的进程状态称为就绪状态。
#
# 二、执行/运行(Running)状态
# 当进程已获得处理机，其程序正在处理机上执行，此时的进程状态称为执行状态。
#
# 三、阻塞(Blocked)状态
# 正在执行的进程，由于等待某个事件发生而无法执行时，便放弃处理机而处于阻塞状态。
# 引起进程阻塞的事件可有多种，例如，等待I/O完成、申请缓冲区不能满足、等待信件(信号)等。

# 同步就是一个任务的完成需要依赖另外一个任务时，
# 只有等待被依赖的任务完成后，依赖的任务才能算完成，
# 这是一种可靠的任务序列。要么成功都成功，失败都失败，两个任务的状态可以保持一致。

# 异步是不需要等待被依赖的任务完成，只是通知被依赖的任务要完成什么工作，
# 依赖的任务也立即执行，只要自己完成了整个任务就算完成了。
# 至于被依赖的任务最终是否真正完成，依赖它的任务无法确定，所以它是不可靠的任务序列。

# 阻塞和非阻塞这两个概念与程序（线程）等待消息通知(无所谓同步或者异步)时的状态有关。
# 也就是说阻塞与非阻塞主要是程序（线程）等待消息通知时的状态角度来说的


# 阻塞和非阻塞这两个概念与程序（线程）等待消息通知(无所谓同步或者异步)时的状态有关。
# 也就是说阻塞与非阻塞主要是程序（线程）等待消息通知时的状态角度来说的

# 进程的创建
# 进程的结束

# python中的进程
# 运行中的程序就是一个进程。所有的进程都是通过它的父进程来创建的。
# 因此，运行起来的python程序也是一个进程，那么我们也可以在程序中再创建进程。

#----------------------------------------------------------------------------------------
# multiprocess模块
"""
multiprocess不是一个模块而是python中一个操作、
管理进程的包。 之所以叫multi是取自multiple的多功能的意思,
在这个包中几乎包含了和进程有关的所有子模块。由于提供的子模块非常多，
为了方便大家归类记忆，我将这部分大致分为四个部分：
创建进程部分，
进程同步部分，
进程池部分，
进程之间数据共享。
"""
# multiprocess.process模块
# process模块是一个创建进程的模块，借助这个模块，就可以完成进程的创建。

# Process(group , target , name , args , kwargs)，
# 由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）

# 强调：
# 1. 需要使用关键字的方式来指定参数
# 2. args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号
#
# 参数介绍：
# 1 group参数未使用，值始终为None
# 2 target表示调用对象，即子进程要执行的任务
# 3 args表示调用对象的位置参数元组，args=(1,2,'kkk',)
# 4 kwargs表示调用对象的字典,kwargs={'name':'kkk','age':18}
# 5 name为子进程的名称

# Process类创建进程的两种方式

# 开进程的方法一:
import time
import random
from multiprocessing import Process


def piao(name):
    print('%s piaoing' % name)
    time.sleep(random.randrange(1, 5))
    print('%s piao end' % name)


if __name__ == '__main__':
    p1 = Process(target=piao, args=('kkk',))  # 必须加,号
    p2 = Process(target=piao, args=('ttt',))
    p3 = Process(target=piao, args=('aaa',))
    p4 = Process(target=piao, args=('bbb',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主线程')

# 开进程的方法二:
import time
import random
from multiprocessing import Process


class Piao(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s piaoing' % self.name)

        time.sleep(random.randrange(1, 5))
        print('%s piao end' % self.name)


if __name__ == '__main__':
    p1 = Piao('ttt')
    p2 = Piao('aaa')
    p3 = Piao('bbb')
    p4 = Piao('ccc')
    p1.start()  # start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    print('主线程')
# 方法介绍
# p.start()：启动进程，并调用该子进程中的p.run()

# p.run():进程启动时运行的方法，正是它去调用target指定的函数，
# 我们自定义类的类中一定要实现该方法

# p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，
# 该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。
# 如果p还保存了一个锁那么也将不会被释放，进而导致死锁

# p.is_alive():如果p仍然运行，返回True

# p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。
# timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，
# 而不能join住run开启的进程

# 属性介绍
# p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，
# 当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，
# 必须在p.start()之前设置

# p.name:进程的名称
# p.pid：进程的pid
# p.exitcode:进程在运行时为None、如果为–N，表示被信号N结束(了解即可)

# p.authkey:进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。
# 这个键的用途是为涉及网络连接的底层进程间通信提供安全性，
# 这类连接只有在具有相同的身份验证键时才能成功（了解即可）




# 强调:在Windows操作系统中由于没有fork(linux操作系统中创建进程的机制)，
# 在创建子进程的时候会自动 import 启动它的这个文件，
# 而在 import 的时候又执行了整个文件。
# 因此如果将process()直接写在文件中就会无限递归创建子进程报错。
# 所以必须把创建子进程的部分使用if _name_ ==‘__main__’ 判断保护起来，
# import 的时候 ，就不会递归运行了。

# 进程间数据隔离
# 进程隔离是为保护操作系统中进程互不干扰而设计的一组不同硬件和软件的技术

# 这个技术是为了避免进程A写入进程B的情况发生。 进程的隔离实现，使用了虚拟地址空间。
# 进程A的虚拟地址和进程B的虚拟地址不同，这样就防止进程A将数据信息写入进程B

# 进程隔离的安全性通过禁止进程间内存的访问可以方便实现
from multiprocessing import Process
n=100

def work():
    global n
    n=0
    print('子进程内: ',n)


if __name__ == '__main__':
    p=Process(target=work)
    p.start()
    print('主进程内: ',n)


# 守护进程

# 会随着主进程的结束而结束。
#
# 主进程创建守护进程

# 　　其一：守护进程会在主进程代码执行结束后就终止

# 　　其二：守护进程内无法再开启子进程,否则抛出异常：
# AssertionError: daemonic processes are not allowed to have children

# 注意：进程之间是互相独立的，主进程代码运行结束，守护进程随即终止

# 守护进程的启动
import os
import time
from multiprocessing import Process

class Myprocess(Process):
    def __init__(self,person):
        super().__init__()
        self.person = person
    def run(self):
        print(os.getpid(),self.name)
        print('%s正在和女主播聊天' %self.person)


p=Myprocess('哪吒')
p.daemon=True #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
p.start()
time.sleep(10) # 在sleep时查看进程id对应的进程ps -ef|grep id
print('主')

# 主进程代码执行结束守护进程立即结束

from multiprocessing import Process

def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")


p1=Process(target=foo)
p2=Process(target=bar)

p1.daemon=True
p1.start()
p2.start()
time.sleep(0.1)
print("main-------")#打印该行则主进程代码结束,则守护进程p1应该被终止.
# #可能会有p1任务执行的打印信息123,因为主进程打印main----时,p1也执行了,但是随即被终止.


# 进程同步(multiprocess.Lock)
# 锁 —— multiprocess.Lock

# 当多个进程使用同一份数据资源的时候，就会引发数据安全或顺序混乱问题。

# 多进程抢占输出资源
import os
import time
import random
from multiprocessing import Process

def work(n):
    print('%s: %s is running' %(n,os.getpid()))
    time.sleep(random.random())
    print('%s:%s is done' %(n,os.getpid()))

if __name__ == '__main__':
    for i in range(3):
        p=Process(target=work,args=(i,))
        p.start()


# 由并发变成了串行,牺牲了运行效率,但避免了竞争
# 使用锁维护执行顺序
import os
import time
import random
from multiprocessing import Process,Lock

def work(lock,n):
    lock.acquire()
    print('%s: %s is running' % (n, os.getpid()))
    time.sleep(random.random())
    print('%s: %s is done' % (n, os.getpid()))
    lock.release()
if __name__ == '__main__':
    lock=Lock()
    for i in range(3):
        p=Process(target=work,args=(lock,i))
        p.start()

# 多进程模拟抢票实例
#文件db的内容为：{"count":1}
#注意一定要用双引号，不然json无法识别
from multiprocessing import Process,Lock
import time,json,random
def search():
    dic=json.load(open('db'))
    print('\033[43m剩余票数%s\033[0m' %dic['count'])

def get():
    dic=json.load(open('db'))
    time.sleep(0.1) #模拟读数据的网络延迟
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(0.2) #模拟写数据的网络延迟
        json.dump(dic,open('db','w'))
        print('\033[43m购票成功\033[0m')

def task():
    search()
    get()

if __name__ == '__main__':
    for i in range(100): #模拟并发100个客户端抢票
        p=Process(target=task)
        p.start()
# 引发问题:数据写入错乱

# 互斥锁保证数据安全
from multiprocessing import Process,Lock
import time,json,random
def search():
    dic=json.load(open('db'))
    print('\033[43m剩余票数%s\033[0m' %dic['count'])

def get():
    dic=json.load(open('db'))
    time.sleep(random.random())  # 模拟读数据的网络延迟
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(random.random())  # 模拟写数据的网络延迟
        json.dump(dic,open('db','w'))
        print('\033[32m购票成功\033[0m')
    else:
        print('\033[31m购票失败\033[0m')

def task(lock):
    search()
    lock.acquire()  # 将买票这一环节由并发变成了串行，牺牲了运行效率但是保证了数据的安全
    get()
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(100):  # 模拟并发100个客户端抢票
        p=Process(target=task,args=(lock,))
        p.start()

# 加锁可以保证多个进程修改同一块数据时，同一时间只能有一个任务可以进行修改，
# 即串行的修改，没错，速度是慢了，但牺牲了速度却保证了数据安全。

# 队列和管道
#因此我们最好找寻一种解决方案能够兼顾：1、效率高（多个进程共享一块内存的数据）
# 2、帮我们处理好锁问题。
# 这就是mutiprocessing模块为我们提供的基于消息的IPC通信机制：队列和管道。

#-------------------------------------------------------------------------------------
# 进程间通信——队列（multiprocess.Queue）
# 创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
# Queue([maxsize])
# 创建共享的进程队列。
# 参数 ：maxsize是队列中允许的最大项数。如果省略此参数，则无大小限制。
# 底层队列使用管道和锁定实现。

# 方法介绍
# Queue([maxsize])
# 创建共享的进程队列。maxsize是队列中允许的最大项数。如果省略此参数，则无大小限制。底层队列使用管道和锁定实现。另外，还需要运行支持线程以便队列中的数据传输到底层管道中。
# Queue的实例q具有以下方法：
#
# q.get( [ block [ ,timeout ] ] )
# 返回q中的一个项目。如果q为空，此方法将阻塞，直到队列中有项目可用为止。
# block用于控制阻塞行为，默认为True. 如果设置为False，
# 将引发Queue.Empty异常（定义在Queue模块中）。timeout是可选超时时间，
# 用在阻塞模式中。如果在制定的时间间隔内没有项目变为可用，将引发Queue.Empty异常。
#
# q.get_nowait( )
# 同q.get(False)方法。
#
# q.put(item [, block [,timeout ] ] )
# 将item放入队列。如果队列已满，此方法将阻塞至有空间可用为止。
# block控制阻塞行为，默认为True。如果设置为False，将引发Queue.Empty异常
# （定义在Queue库模块中）。timeout指定在阻塞模式中等待可用空间的时间长短。
# 超时后将引发Queue.Full异常。
#
# q.qsize()
# 返回队列中目前项目的正确数量。此函数的结果并不可靠，
# 因为在返回结果和在稍后程序中使用结果之间，队列中可能添加或删除了项目。
# 在某些系统上，此方法可能引发NotImplementedError异常。
#
#
# q.empty()
# 如果调用此方法时 q为空，返回True。如果其他进程或线程正在往队列中添加项目，结果是不可靠的。也就是说，在返回和使用结果之间，队列中可能已经加入新的项目。
#
# q.full()
# 如果q已满，返回为True. 由于线程的存在，结果也可能是不可靠的（参考q.empty（）方法）。。


# 了解内容
# q.close()
# 关闭队列，防止队列中加入更多数据。调用此方法时，
# 后台线程将继续写入那些已入队列但尚未写入的数据，
# 但将在此方法完成时马上关闭。如果q被垃圾收集，将自动调用此方法。
# 关闭队列不会在队列使用者中生成任何类型的数据结束信号或异常。
# 例如，如果某个使用者正被阻塞在get（）操作上，
# 关闭生产者中的队列不会导致get（）方法返回错误。

# q.cancel_join_thread()
# 不会再进程退出时自动连接后台线程。这可以防止join_thread()方法阻塞。

# q.join_thread()
# 连接队列的后台线程。此方法用于在调用q.close()方法后，等待所有队列项被消耗。
# 默认情况下，此方法由不是q的原始创建者的所有进程调用。
# 调用q.cancel_join_thread()方法可以禁止这种行为。

# 单看队列用法
'''
multiprocessing模块支持进程间通信的两种主要形式:管道和队列
都是基于消息传递实现的,但是队列接口
'''

from multiprocessing import Queue
q=Queue(3)

#put ,get ,put_nowait,get_nowait,full,empty
q.put(3)
q.put(3)
q.put(3)
# q.put(3)   # 如果队列已经满了，程序就会停在这里，等待数据被别人取走，再将数据放入队列。
           # 如果队列中的数据一直不被取走，程序就会永远停在这里。
try:
    q.put_nowait(3) # 可以使用put_nowait，如果队列满了不会阻塞，但是会因为队列满了而报错。
except: # 因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下去，但是会丢掉这个消息。
    print('队列已经满了')

# 因此，我们再放入数据之前，可以先看一下队列的状态，如果已经满了，就不继续put了。
print(q.full()) #满了

print(q.get())
print(q.get())
print(q.get())
# print(q.get()) # 同put方法一样，如果队列已经空了，那么继续取就会出现阻塞。
try:
    q.get_nowait(3) # 可以使用get_nowait，如果队列满了不会阻塞，但是会因为没取到值而报错。
except: # 因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下去。
    print('队列已经空了')

print(q.empty()) #空了
# 上面这个例子还没有加入进程通信，只是先来看看队列为我们提供的方法，以及这些方法的使用和现象。


# 子进程给父进程发数据
import time
from multiprocessing import Process, Queue

def f(q):
    q.put([time.asctime(), 'from Eva', 'hello'])  #调用主函数中p进程传递过来的进程参数 put函数为向队列中添加一条数据。

if __name__ == '__main__':
    q = Queue() #创建一个Queue对象
    p = Process(target=f, args=(q,)) #创建一个进程
    p.start()
    print(q.get())
    p.join()

#上面是一个queue的简单应用，
# 使用队列q对象调用get函数来取得队列中最先进入的数据。 接下来看一个稍微复杂一些的例子

# 批量生产数据放入队列再批量获取结果 x
import os
import time
import multiprocessing

# 向queue中输入数据的函数
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.asctime())
    queue.put(info)

# 向queue中输出数据的函数
def outputQ(queue):
    info = queue.get()
    print ('%s%s\033[32m%s\033[0m'%(str(os.getpid()), '(get):',info))

# Main
if __name__ == '__main__':
    multiprocessing.freeze_support()
    record1 = []   # store input processes
    record2 = []   # store output processes
    queue = multiprocessing.Queue(3)

    # 输入进程
    for i in range(10):
        process = multiprocessing.Process(target=inputQ,args=(queue,))
        process.start()
        record1.append(process)

    # 输出进程
    for i in range(10):
        process = multiprocessing.Process(target=outputQ,args=(queue,))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    for p in record2:
        p.join()






# 基于队列实现进程间通信
import time
from multiprocessing import Process, Queue
def f(q):
    q.put('hello')  #调用主函数中p进程传递过来的进程参数 put函数为向队列中添加一条数据。
if __name__ == '__main__':
    q = Queue()  # 创建一个Queue对象
    p = Process(target=f, args=(q,)) #创建一个进程
    p.start()
    print(q.get())  # 从队列中获取数据
    p.join()


from multiprocessing import Queue,Process
def producer(q):
    q.put('hello big baby!')
def consumer(q):
    print(q.get())
if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer,args=(q,))
    p.start()
    p1 = Process(target=consumer,args=(q,))
    p1.start()



# 生产者消费者模型
# 在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。
# 该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

# 生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。
# 生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，
# 所以生产者生产完数据(做包子的)之后不用等待消费者(吃包子的)处理，
# 直接扔给阻塞队列(盘子)，消费者不找生产者要数据，而是直接从阻塞队列里取，
# 阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

# 在线程世界里，生产者就是生产数据的线程，
# 消费者就是消费数据的线程。在多线程开发当中，
# 如果生产者处理速度很快，而消费者处理速度很慢，
# 那么生产者就必须等待消费者处理完，才能继续生产数据。
# 同样的道理，如果消费者的处理能力大于生产者，
# 那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

# 基于队列实现生产者消费者模型
from multiprocessing import Process,Queue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('%s 吃 %s' %(os.getpid(),res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        q.put(res)
        print('%s 生产了 %s' %(os.getpid(),res))

if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))

    #开始
    p1.start()
    c1.start()
    print('主')

# 此时的问题是主进程永远不会结束，原因是：生产者p在生产完后就结束了，
# 但是消费者c在取空了q之后，则一直处于死循环中且卡在q.get()这一步。
#
# 解决方式无非是让生产者在生产完毕后，往队列中再发一个结束信号，
# 这样消费者在接收到结束信号后就可以break出死循环。

# 改良版——生产者消费者模型
from multiprocessing import Process,Queue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        if res is None:break #收到结束信号则结束
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))
    q.put(None) #发送结束信号
if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))

    #开始
    p1.start()
    c1.start()
    print('主')

# 注意：结束信号None，不一定要由生产者发，
# 主进程里同样可以发，但主进程需要等生产者结束后才应该发送该信号
# 主进程在生产者生产完毕后发送结束信号None
from multiprocessing import Process,Queue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        if res is None:break #收到结束信号则结束
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(q):
    for i in range(2):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))

if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))

    #开始
    p1.start()
    c1.start()

    p1.join()
    q.put(None) #发送结束信号
    print('主')

# 在有多个生产者和多个消费者时，我们则需要用一个很low的方式去解决
