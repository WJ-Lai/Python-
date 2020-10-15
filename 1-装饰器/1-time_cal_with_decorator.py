import time
def timer(function):
    def wrapper():
        time_start = time.time()
        function()
        time_end = time.time()
        cost_time = time_end - time_start
        print("花费时间：{}秒".format(cost_time))
    return wrapper

@timer
def func1():
    print('我是一个函数1')

@timer
def func2():
    print('我是一个函数2')

@timer
def func3():
    print('我是一个函数3')

if __name__ == '__main__':
    func1()
    func2()
    func3()

