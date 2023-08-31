#one way to share date between processes is by using queue

import multiprocessing

def square(numbers,q):
    for n in numbers:
        q.put(n*n)
     
if __name__=="__main__":
    array= [2,3,8,9]
    q = multiprocessing.Queue()
    p1= multiprocessing.Process(target=square, args=(array,q))
    
    p1.start()
    p1.join()

    while q.empty() is False:
        print (q.get())
