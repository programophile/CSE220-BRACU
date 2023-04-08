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
    def PrintLL(self):
        temp=self.head
        while temp!=None:
            print(temp.elem,end=" ")
            temp=temp.next

    def LastFront(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        last=temp.next
        second_first = self.head.next
        temp.next=self.head
        self.head=last
        self.head.next=second_first
        temp.next.next=None
a=[1,2,4,5,6]
b=LinkedList(a)
b.LastFront()
b.PrintLL()
