from multiprocessing import Pool
import time

def sum(n):
    sum=0
    for x in range(10000):
        sum += x*x
    return sum

if  __name__=="__main__":
    # array=[1,2,3,4,5]
    t1=time.time()
    p=Pool(processes=4)
    result=p.map(sum,range(1000))
    p.close()
    p.join()

    print("time took by pool is : ",time.time()-t1)

    t2=time.time()
    result=[]
    for x in range(10000):
        result.append(sum(x))

    print("time took is : ",time.time()-t2)
