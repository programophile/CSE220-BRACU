class Node:
    def __init__(self,elem,next):
        self.elem=elem
        self.next=next
class LinkedList:
    def __init__(self,array):
        self.head=None
        tail=None
        for i in range(len(array)):
            n = Node(array[i], None)
            if self.head==None:
                self.head=n
                tail=n
            else:
                tail.next=n
                tail=n
        tail.next=self.head.next.next
    def PrintLL(self):
        temp=self.head
        while temp!=None:
            print(temp.elem,end=" ")
            temp=temp.next
