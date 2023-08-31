#one way to share date between processes is by using array
import multiprocessing

def square(numbers, result,v):
    v.value=3.09  #Assigning a value
    for idx,n in enumerate(numbers):
        result[idx] = n*n
    

if __name__=="__main__":
    array= [2,3,8,9]
    result = multiprocessing.Array('i',4)
    v= multiprocessing.Value('d',0.0)
    p1= multiprocessing.Process(target=square, args=(array,result,v))
    
    p1.start()

    p1.join()

    print("Outside result",result[:])
    print("printing value : ",v.value)
    print("Done")
