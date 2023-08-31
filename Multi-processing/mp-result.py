#Multiprocessing uses different address space for each process

import time
import multiprocessing

result= []

def square(numbers):
    global result
    for n in numbers:
        result.append(n*n)
    
    print("within the process : ",result )



if __name__=="__main__":
    array= [2,3,8,9]
    p1= multiprocessing.Process(target=square, args=(array,))
    p1.start()

    p1.join()

    print("outside the process : ",result )
    print("Done")
