import time
def func1():
    time_start = time.time()
    print('我是一个函数1')
    time_end = time.time()
    cost_time = time_end - time_start
    print("花费时间：{}秒".format(cost_time))

def func2():
    time_start = time.time()
    print('我是一个函数2')
    time_end = time.time()
    cost_time = time_end - time_start
    print("花费时间：{}秒".format(cost_time))

def func3():
    time_start = time.time()
    print('我是一个函数3')
    time_end = time.time()
    cost_time = time_end - time_start
    print("花费时间：{}秒".format(cost_time))

if __name__ == '__main__':
    func1()
    func2()
    func3()



