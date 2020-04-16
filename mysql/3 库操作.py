#__author__ = 'Winston'
#date: 2020/4/10

# information_schema： 虚拟库，不占用磁盘空间，存储的是数据库启动后的一些参数，如用户表信息、
# 列信息、权限信息、字符信息等

# performance_schema： MySQL 5.5开始新增一个数据库：主要用于收集数据库服务器性能参数，
# 记录处理查询请求时发生的各种事件、锁等现象

# mysql： 授权库，主要存储系统用户的权限信息

# test： MySQL数据库系统自动创建的测试数据库

# CREATE DATABASE 数据库名 charset utf8;
# 可以由字母、数字、下划线、＠、＃、＄
# 区分大小写
# 唯一性
# 不能使用关键字如 create select
# 不能单独使用数字
# 最长128位

# 1 查看数据库
# show databases;
# show create database db1;
# select database();
#
# 2 选择数据库
# USE 数据库名
#
# 3 删除数据库
# DROP DATABASE 数据库名;
#
# 4 修改数据库
# alter database db1 charset utf8;