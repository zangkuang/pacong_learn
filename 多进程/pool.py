# -*- coding: utf-8 -*-
# author:lyz
# time:2021/5/5  20:07 
# tool：PyCharm

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool(8)  # 定义pool,cpu核数量为4
    # res = pool.map(job, range(100000000))  # 获取结果,函数及需迭代运算的值
    # print(res)
    '''
    Pool除了map()外，还有可以返回结果的方式，那就是apply_async()
    apply_async()中只能传递一个值，它只会放入一个核进行运算
    但是传入值时要注意是可迭代的，所以在传入值后需要加逗号, 同时需要用get()方法获取返回值'''
    res = pool.apply_async(job,(2,))        #async为异步意思
    #用get获取结果
    print(res.get())

    # apply_async()输出多个结果,迭代器
    multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
    #取值也需要一个个取
    print([res.get() for res in multi_res])
if __name__ == '__main__':
    multicore()

