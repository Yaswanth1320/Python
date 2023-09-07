#LinkedList implementation in python

# Creating a Node class
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#Creating a LinkedList class
class LinkedList:
    def __init__(self):
        self.head=None

    #method for inserting at first
    def insertAtFirst(self,data):
        node = Node(data,self.head)
        self.head = node 

    #method to insert element at last
    def insertAtLast(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None) 

    #Inserting a list of values by using list tuple
    def insert_multiple(self,data_list):
        self.head = None
        for data in data_list:
            self.insertAtLast(data)


    # to find the length of linkedlist
    def length(self):
        len = 0
        itr = self.head
        while itr:
            len += 1 
            itr = itr.next
        
        return len
    
    # insert at particular index
    def insertAtIndex(self,index,data):
        if index == 0 or index == self.length():
            raise Exception("invalid index")
        
        if index == 0:
            self.insertAtFirst()
            return
        
        len = 0
        itr = self.head
        while itr:
            if len == index -1:
                node = Node(data ,itr.next)
                itr.next=node
                break

            itr = itr.next
            len += 1
        
        
    # remove at particular index
    def removeAtIndex(self,index):
        if index == 0 or index == self.length():
            raise Exception("invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        len = 0
        itr = self.head
        while itr:
            if len == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            len += 1
        
     
    # to diaplay the LinkedList
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        linkList=''

        while itr:
            linkList += str(itr.data) + "-->"
            itr = itr.next

        print(linkList)   
        

#Drive Code

if __name__ == "__main__":
    ll = LinkedList()    # creating a object for linkedList class
    ll.insertAtFirst(5)
    ll.insertAtLast(10)
    ll.insertAtLast(20)
    ll.insertAtLast(30)
    ll.insertAtLast(40)
    # ll.insert_multiple([10,20,30,40])
    ll.removeAtIndex(2)
    ll.insertAtIndex(2,20)
    ll.display()

