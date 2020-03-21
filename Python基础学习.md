# Python基础学习

## 字符编码

早先的ASCII编码只能表示一些字母，数字和符号，但是处理中文是不够用的，所以中国制定了GB2312编码来表示中文，但是这样的话一个国家就会有一套自己的编码格式，所以在这种情况下，Unicode编码应运而生

**Unicode**将所有语言都统计到一套编码中，这样就不会再有乱码的问题出现，常用的是用两个字节来表示一个字符，特别生僻的字就需要用四个字节来表示，在便利的条件下，又一个新的问题就出现了，同一个字符A，用ASCII来表示就是`01000001`，用Unicode来表示就是`00000000 01000001`，如果写的文章基本上都是英文，那么使用Unicode编码就比ASCII编码多一倍的存储空间，在存储和传输上就非常不划算

本着节约的精神，出现了将Unicode编码转换为可变长编码的UTF-8编码，UTF-8将一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成一个字节，汉字三个字节，传输的文本包含大量英文字符，使用起来就非常节省空间

**在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者传输时就会转换为UTF-8编码，在浏览网页时，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器**

- python提供了`ord()`函数获取字符的整数表示，`chr()`将编码转换为对应字符

    ```python
    In [1]: ord('A')
    Out[1]: 65
    
    In [2]: ord('中')
    Out[2]: 20013
    
    In [3]: chr(66)
    Out[3]: 'B'
    
    In [4]: chr(25991)
    Out[4]: '文'
    ```

- Python的字符串类型时str，在内存是Unicode，一个字符对应若干个字节，如果要在网络上传输，或者保存在磁盘上，就需要把str变为以字节为单位的bytes

- python`len()`函数计算的是str的字符数，如果换成bytes，len就会计算字节数

- **函数可变参数**：在函数参数出加了一个*，在函数内部接收到的是一个tuple

- **命名关键字参数**：限制关键字参数的名字

    `def person(name, age, *, city, job)`

    只接受city和job作为关键字参数

- 参数定义的顺序：

    1. 必选参数
    2. 默认参数
    3. 可变参数
    4. 命名关键字参数
    5. 关键字参数

- for循环关键字可以用作可迭代对象之上

    通过`isinstance('ac', Iterable)`

- python内置的`enumerate`可以将一个list元素变为**索引-元素对象**

    ```python
     for i, value in enumerate(A):
     		print('the index %d is %s' % (i, value))
    ```

- 列表生成式：`list(x*x for x in range(1, 11))`, `list(x*x for x in range(1, 11) if x%2 == 0)`

- python三目运算符：`smaller = x if x < y else y`

	## 生成器（Generator）

通过列表生成器可以直接创建一个列表，但是内存限制列表容量，可以根据某种算法推算，在循环的过程中不断推算后续的元素，在python中，这种一遍循环一边计算的机制称作生成器。

```python
In [17]: L = (x * x for x in range(1, 11))

In [18]: L
Out[18]: <generator object <genexpr> at 0x107aae228>

In [19]: next(L)
Out[19]: 1

In [20]: next(L)
Out[20]: 4

In [21]: next(L)
Out[21]: 9
```

可以看出，生成器与列表生成器的不同就在于[],()的区别，可以使用next()来获取生成器的下一个元素

当然，也可以使用for来遍历，因为生成器本质上也是一个可迭代对象

```python
In [24]: isinstance(L, Iterable)
Out[24]: True
  
  
In [24]: isinstance(L, Iterable)
Out[24]: True

In [25]: for val in L:
    ...:     print(val)
    ...:
16
25
36
49
64
81
100
```

在创建一个生成器之后，正确的做法是不会使用next，而是直接使用for来进行遍历，并且也不用担心StopIteration

如果有别的需求，仅仅一行无法实现生成器时，那么还可以使用函数来实现，比如著名的斐波那契数列，仅仅一个for循环是无法实现的，用函数实现输出斐波那契数列的前N个数

```python
# max代表是几个数，从1，1，2开始
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'
```

可以看出fib函数的推算规则，从第一个元素开始，推算后续的任意元素，这种逻辑和generator非常相似，所以只需要将fib函数变为generator，只需要将print(b)改写为yield b即可

```python
# fib generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
```

这就是定义generator的另一个方法。**如果一个函数定义中包含yield关键字，那么这个函数就不是一个普通函数，而是一个generator**

```python
In [33]: g = fib(6)

In [34]: print(g)
<generator object fib at 0x1079fb138>
```

要理解函数和generator的执行流程。普通函数是顺序执行，遇到return语句或者执行到最后一行函数语句就会返回。generator函数在每次调用next()执行，遇到`yield`语句返回，再次执行时就会从上次返回的yield语句处再执行

使用for来迭代

```python
In [35]: for val in g:
    ...:     print(val)
    ...:
1
1
2
3
5
8
```

但是使用for来迭代generator时，会获取不到返回值，如果想要拿到返回值，就必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中

```python
while True:
    ...:     try:
    ...:         x = next(g)
    ...:         print('g:', x)
    ...:     except StopIteration as e:
    ...:         print('Generator return value:', e.value)
    ...:         break
```

普通函数调用直接返回结果

```python
r = abs(6)
r
6
```

generator函数的调用实际返回一个generator对象

```python
>>> g = fib(6)
>>> g
<generator object fib at 0x1022ef948>
􏱷 
```

## 迭代器

可以直接用作于for循环的对象成为可迭代对象：`Iterable`，可以用`isinstance`判断

可以被next函数调用并且不断返回下一个值的对象成为迭代器：`Iterator`

生成器都是`Iterator`对象，但是`list`，`dict`，`str`虽然是`Iterable`，却不是`Iterator`，可以使用`Iter()`函数将`Iterable`变为`Iterator`

![image-20200320133808714](/Users/zhangmingyi/Desktop/Python基础学习.assets/image-20200320133808714.png)

## 高阶函数

#### map/reduce

**map**传入的第一个参数是函数对象本身，结果是一个Iterator，可以理解为将list的每一个元素都作用于f(x)并生成一个新的list

```python
In [41]: def func(x):
    ...:     return x * x
    ...:

In [42]: res = map(func, [1, 2, 3, 4, 5])

In [43]: print(res)
<map object at 0x10959da20>

In [44]: list(res)
Out[44]: [1, 4, 9, 16, 25]
```

将list的所有数据转换为字符：`list(map(str, [1, 2, 3]))`

**reduce**将一个函数作用在一个序列上，这个函数接受两个参数，reduce把结果继续和序列的下一个元素做累计计算，其效果就是

`reduce(func, [x1, x2, x3, x4]) = func(func(func(x1, x2), x3), x4)`

eg: 一个序列求和

```python
from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 2, 3])
6
```

map与reduce配合写出str转int

```python
from functools import reduce

def func(x, y):
    return x * 10 + y

def str_to_int(s):
    digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    return digits[s]

print(reduce(func, map(str_to_int, '12345')))


# 整理成一个函数
DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    
    def char2num(c):
        return DIGITS[c]
    
    return reduce(fn, map(char2num, s))
```

#### filter

Python内置的filter函数用于过滤序列，与map类似，filter也接受一个函数和一个序列，只不过filter会根据函数的返回值来确定是保留还是丢弃

删掉一个序列中的空字符串

```python
def space(s):
    return s and s.strip()

list(filter(space, ['aa', 'v', '', 'aa']))
```

filter这个函数关键在于一个筛选，

#### sorted

可以接受一个key函数来实现自定义的排序，按绝对值大小排序

`sorted([31, 12, -12, 11], key=abs)`

忽略大小写

`sorted('aa', 'BB', 'Ab', 'aB', key=str.lower)`

如果要进行反向排序，那么可以传入第三个参数

`sorted('aa', 'BB', 'Ab', 'aB', key=str.lower, reverse=True)`

## 函数作为返回值

### 闭包（Closure）

返回的函数在其定义内部引用了局部变量args，所以一个函数返回了另一个函数之后其内部的局部变量还被新的函数引用

返回的函数没有立即执行，而是调用了f()才执行

```python
def count():
    res = []
    for i in range(1, 4):
        def func():
            print(i * i)
            return None
        res.append(func)
    return res

f1, f2, f3 = count()

f1()
f2()
f3()

9
9
9
```

产生这种问题的原因在于引用了变量i，但是她并非是立即执行，等到3个函数都返回，那么引用的变量都是3，所以最终的结果是9

返回闭包时必须牢记：**返回函数不要返回任何循环变量，或者后续会发生变化的变量**，如果非要引用循环变量，那就需要再创建一个函数，用该函数的参数绑定循环变量当前的值，无论后续如何修改，已经绑定到函数的参数值不变

```python
def count():
    def fnuc(j):
        def g():
            return j * j
        return g
    
    res = []
    for i in range(1, 4):
        res.append(func(i))

    return res
```

### 匿名函数（lambda）

### 装饰器

如果要修改某个函数的功能，比如在函数调用前后自动添加打印日志，但是又不希望修改当前函数定义，这种在代码运行期间动态增加功能的方式称为装饰器（Decorator）

```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2020-02-02')
```

将@log放在now函数的定义处，相当于执行了`now = log(now)`

log是一个decorator，返回一个函数，原来的now函数仍然存在，只是现在now变量指向新的函数，即在log中返回的wrapper()函数

如果需要给decorator传入参数，就需要编写一个返回decorator的高阶函数

```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*agrs, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2020-02-02')      
```

和两层嵌套的decorator相比，三层嵌套的效果是这样的

`now = log('execute')(now)`

执行log('execute')，返回的是decorator函数，再调用返回的decorator，参数是now函数，最终的返回结果是wrapper

但是现在又有一个问题，如果输出`now.__name__`，那么已经变成`wrapper`，在python中，一切都是对象，now不是函数，只是指向了函数，经过装饰之后，now指向的函数发生了变化，所以活着函数的属性也发生了变化，所以为了避变有些需要用到这些属性的情况，我们需要作出一点小改变来实现一个完整`decorator`

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*agrs, **kw)
    return wrapper


# 针对带参数的装饰器
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
            
```

## IO

### 操作文件和目录

```python
import os
# 查看当前目录的绝对路径
os.path.abspath('.')

#将两个目录合成一个时，不要直接拼接字符串，这样可以正确处理不同操作系统的路径分隔符
os.path.join()
        
# 拆分路径的函数不要直接拆分，后一部分总是最高级别的目录或者文件名
os.path.split()

# 直接得到文件扩展名
os.path.splirtext('/User/zmy/test.txt')
```

TODO: 序列化和反序列化，Json



## 进程/线程/协程

### 进程

```python
import os

print('Process (%s) start ...' % os.getpid())

pid = os.fork()

if pid == 0:
    print("I'm child process (%s) and my parent is %s." % (os.getpid(), os.getppid()))
else:
    print("I (%s) just create a child process (%s)." % (os.getpid(), pid))
```

#### multiprocessing

因为在win平台上没有fork系统调用，所以python本身也是提供了一个跨平台的多进程支持，`multiprocessing`就是跨平台版本的多进程模块，这个模块提供了一个`Process`来代表一个进程对象，下面是一个启动子进程并等待其结束

```python
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))
    

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end')
```

用这种方式创建子进程，只需要传入一个执行函数和执行函数的参数，用start方式启动，这样比fork还要简单

#### Process Pool

如果要大量的进程，可以使用进程池的方式来批量创建子进程

```python
from multiprocessing import Pool
import os
import time 
import random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    
    
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
        
    print('Waiting for all subprocess done...')
    p.close() # 调用之后不能添加新的process
    p.join()
    print('All subprocess done.')
```

#### 进程间通信

multiprocessing内部提供了多种机制来实现进程之间的通信，比如Queue，Pipes等多种方式

```python
from multiprocessing import Process, Queue
import os
import time
import random

# 写进程执行代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for val in ['A', 'B', 'C']:
        print('Put %s to queue...' % val)
        q.put(val)
        time.sleep(random.random())
        

# 读进程执行代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        val = q.get(True)
        print('Get %s from queue.' % val)
        
 
if __name__ == '__main__':
    # 父进程创建queue，并传递给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate() # 读进程是死循环，无法等待其自动结束，强行退出
```

### 线程

Python的线程是真正的Posix Thread，而不是模拟出来的线程，Python的标准库提供了两个模块`_thread`和`threading`，threading对_thread进行了封装。

```python
import time
import threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
    print('thread %s enden.' % threading.current_thread().name)
   

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)
```

#### 线程加锁问题

```python
def chang_it(n):
    # 先存后取结果为0
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000000):
        chang_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
```

如果要保证balance正确，就要给change_it上一把锁

```python
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(1000):
        lock.acquire() # 先获取锁
        try:
            change_it(n)
        finally:
            lock.release()
```

获得锁的线程用完之后一定要释放锁，否则那些等待锁的线程将会永远等待下去，成为死线程，所以使用try...finally来确保锁一定会被释放

#### TheadLocal

```python
local_school = threading.local()

def process_thread(name):
    local_school.student = name
    process_student()


def process_student():
    stu = local_school.student
    print('Hello %s in (%s)' % (stu, threading.current_thread().name))


t1 = threading.Thread(target=process_thread, args=('lili',), name='thread1')
t2 = threading.Thread(target=process_thread, args=('nene',), name='thread2')
t1.start()
t2.start()
t1.join()
t2.join()
```

全局变量local_school就是一个ThreadLocal对象，每个thread都可以读取其属性，但是互不影响，不用管理锁的问题

常用的地方就是为每个线程绑定一个数据连接，HTTP请求，用户身份信息。

### 计算密集型vsIO密集型

### 异步IO

### 分布式进程































