class Node:
    def __init__(self,elem,next):
        self.elem=elem
        self.next=next
class LinkedList:
    def __init__(self,array,starting_index):
        self.array=array
        self.st_index=starting_index
        self.head=None
        tail=None
        for i in range(len(array)):
            n=Node(array[self.st_index],None)
            if self.head==None:
                self.head=n
                tail=n
            else:
                tail.next=n
                tail=n
            self.st_index-=1
            if self.st_index==-1:
                self.st_index=len(array)-1
    def printll(self):
        temp=self.head
        while temp:
            print(temp.elem,end=" ")
            temp=temp.next
        print()
    def reverse(self,temp):

        if temp==None:
            return
        else:
            self.reverse(temp.next)
            print(temp.elem)


a=LinkedList([40,10,20,0,60,30,50],2)
a.printll()
a.reverse(a.head)