# -*- coding: utf-8 -*-
# author:lyz
# time:2021/5/5  19:45 
# tool：PyCharm

import multiprocessing as mp
import threading as td

# multiprocessing和threading
"""def job(a, d):
    print('aaaa')

if __name__ == '__main__':      # before running,must define main:
    # creation Thread and Process
    t1 = td.Thread(target=job, args=(1, 2))
    p1 = mp.Process(target=job, args=(1, 2))
    # 启动线程和进程
    t1.start()
    p1.start()
    # 连接线程和进程
    t1.join()
    p1.join()"""

#multiprocessing Queue
"""import multiprocessing as mp

def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue

if __name__=='__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))       # 参数后面需要加一个逗号,表示args可迭代,不加会报错
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1,res2)
    print(res1+res2)"""

# 效率对比 threading&multiprocessing
"""def job(q):
    res = 0
    for i in range(1000000):
        res += i + i**2 + i**3
    q.put(res) # queue

def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1 + res2)

def multithread():
    q = mp.Queue() # thread可放入process同样的queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)

def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i**2 + i**3
    print('normal:', res)

import time

if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)"""