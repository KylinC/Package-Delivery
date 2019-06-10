import multiprocessing as mp
import threading as td
import time

def job(q):
    res=0
    for i in range(1000000):
        res += i+i**2+i**3
        res /= i**3+1
    q.put(res)

def normal(num):
    res = 0
    result = 0
    for _ in range(num):
        res = 0
        for i in range(1000000):
            res += i + i**2 + i**3
            res /= i**3+1
        result += res
    print('normal:', result)

def multicore(Process_num):
    q = mp.Queue()
    process=[]
    result=0
    for idx in range(Process_num):
        process.append(mp.Process(target=job, args=(q,)))
        process[idx].start()
    for idx in range(Process_num):
        process[idx].join()
        result += q.get()
    print('multicore:', result)


if __name__ == '__main__':
    st = time.time()
    normal(8)
    st1 = time.time()
    print('normal time:', st1 - st)
    st2 = time.time()
    multicore(8)
    print('multicore time:', time.time() - st2)