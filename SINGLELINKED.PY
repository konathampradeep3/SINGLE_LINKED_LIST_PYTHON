class Node:
    def __init__(self,data):
        self.data=data
        self.next=None    #address of next node
class Single():
    def __init__(self):
        self.head=None    

    def insert_begin(self,data):    #insertion at begining
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def insert_end(self,data):    #insertion at ending
        nne=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=nne

    def insert_index(self,data):     #insertion at specific index position
        pos=4
        newindex=Node(data)  
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        newindex.data=data
        newindex.next=temp.next
        temp.next=newindex   


    def delete_begin(self):        
        temp=self.head
        self.head=temp.next
        temp.next=None


    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None


    def delete_insert(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None



    
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end='-->')
                temp=temp.next  

    def rev(self):         #reverse
        prev=None
        temp=self.head
        while temp:
            new=temp.next
            temp.next=prev
            prev=temp
            temp=new
        self.head=prev 


    def palindrome(self):     #check palindrome or not
        stack=[]
        temp=self.head
        while temp:
            stack.append(temp.data)
            temp=temp.next
        temp=self.head
        while temp:
            if temp.data!=stack.pop():
                return False
            temp=temp.next
        return True
    

    def count(self):   #count
        self.count=0
        temp=self.head
        while temp:
            self.count+=1
            temp=temp.next
        return self.count  



    def middle(self):     #find the middle of the linked list
        slow=self.head
        fast=self.head
        while fast!=None and  fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow.data  


    def sortedremove(self):    #remove the duplicates from sorted 
        temp=self.head
        while temp and temp.next:
            if temp.data!=temp.next.data:
                temp=temp.next
            else:
                temp.next=temp.next.next 


    def unsortedremove(self):
        temp=self.head
        prev=None
        s=set()
        while temp:
            if temp.data not in s:
                s.add(temp.data)
                prev=temp
                temp=temp.next
            else:
                prev.next=temp.next
                temp=temp.next  

           
l=Single() 
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
l.insert_begin(15)
l.insert_end(69)
l.insert_index(56)
l.delete_begin()
l.delete_end()
l.delete_insert(3)
l.rev()
print(l.palindrome())
print(l.count())
print(l.middle())
l.remove()
l.unsortedremove()
l.display()





