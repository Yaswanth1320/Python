import time
import threading

def square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('square',n*n)

def cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('cube',n*n*n)

arr=[2,3,8,9]

t=time.time()

t1=threading.Thread(target=square,args=(arr,))
t2=threading.Thread(target=cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

 


