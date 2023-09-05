#Python implementation of linear search

def linearSearch(array_list,value_to_find):
    for index, element in enumerate(array_list):
        if element == value_to_find:
            return index
        
    return -1
    

if __name__ == "__main__":
    array_list = [20,30,50,80,90]
    value = 90
    index = linearSearch(array_list,value)
    print(f"The value is in the {index} index of the array_list")
    
