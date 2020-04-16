#__author__ = 'Winston'
#date: 2020/3/31

# r:以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# w:打开一个文件只用于人。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a:打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# rb:以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# wb:以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab:以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写人到已有内容之后。如果该文件不存在，创建新文件进行写人。
# r+:打开一个文件用于读写。文件指针将会放在文件的开头。
# w+:打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+:打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# rb+:以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# wb+:以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab+:以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，则创建新文件用于读写.

# 读
# f.read()  # 读取所有内容,执行完该操作后，文件指针会移动到文件末尾 如果内容过大会导致内存溢出
# f.readline()  # 读取一行内容,光标移动到第二行首部
# f.readlines()  # 读取每一行内容，以换行符分割,存放于列表中 如果内容过大会导致内存溢出

#f = open('design_model.txt',encoding = 'utf-8')
#print(f.read())
with open('design_model.txt',encoding = 'utf-8') as f:
    print(f.readline())

# 大数据量分段读取
# 方式一
# with open('design_model.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         print(line) # 同一时刻只读入一行内容到内存中
#
# # 方式二
# with open('design_model.txt',mode='rb') as f:
#     while True:
#         data=f.read(1024) # 同一时刻只读入1024个Bytes到内存中
#         if len(data) == 0:
#             break
#         print(data)

# f.readable()  # 文件是否可读
# f.writable()  # 文件是否可读
# f.closed  # 文件是否关闭
# f.encoding  # 如果文件打开模式为b,则没有该属性
# f.flush()  # 立刻将文件内容从内存刷到硬盘

# 光标操作
# f.seek(指针移动的字节数,模式控制):
# 模式控制:
# 0: 默认的模式,该模式代表指针移动的字节数是以文件开头为参照的
# 1: 该模式代表指针移动的字节数是以当前所在的位置为参照的
# 2: 该模式代表指针移动的字节数是以文件末尾的位置为参照的
# 强调:其中0模式可以在t或者b模式使用,而1跟2模式只能在b模式下用
# f.tell() 查看当前文件指针距离文件开头的位置

# 模拟进度条
import sys,time

for i in range(40):
    sys.stdout.write('#')
    sys.stdout.flush()     #flush强制舒心缓存到内存的数据写入硬盘
    time.sleep(0.1)


# 文件修改的本质：将硬盘中文件内容读入内存,然后在内存中修改完毕后再覆盖回硬盘
# 方式一
# 实现思路：将文件内容发一次性全部读入内存,然后在内存中修改完毕后再覆盖写回原文件
# 优点: 在文件修改过程中同一份数据只有一份
# 缺点: 会过多地占用内存
# with open('db.txt',mode='rt',encoding='utf-8') as f:
#     data=f.read()
#
# with open('db.txt',mode='wt',encoding='utf-8') as f:
#     f.write(data.replace('xxxx','yyyy'))

# 方式二
# 实现思路：以读的方式打开原文件,以写的方式打开一个临时文件,一行行读取原文件内容,修改完后写入临时文件...,删掉原文件,将临时文件重命名原文件名
# 优点: 不会占用过多的内存
# 缺点: 在文件修改过程中同一份数据存了两份
import os

with open('db.txt',mode='rt',encoding='utf-8') as read_f,\
        open('.db.txt.swap',mode='wt',encoding='utf-8') as wrife_f:
    for line in read_f:
        wrife_f.write(line.replace('xxxx','yyyy'))

os.remove('db.txt')
os.rename('.db.txt.swap','db.txt')