#the main difference between multi threading and multi processing is multiprocessing has seperate or unique ipc(address) for each process 


import time
import multiprocessing

def square(numbers):
    for n in numbers:
        time.sleep(5)
        print(" sqaure " + str(n*n))

def cube(numbers):
    for n in numbers:
        time.sleep(5)
        print(" cube " + str(n*n*n))


if __name__=="__main__":
    array= [2,3,8,9]
    p1= multiprocessing.Process(target=square, args=(array,))
    p2= multiprocessing.Process(target=cube, args=(array,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
