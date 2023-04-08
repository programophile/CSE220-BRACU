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
        # tail.next=self.head.next
    def PrintLL(self):
        temp=self.head
        while temp!=None:
            print(temp.elem,end=" ")
            temp=temp.next
def CheckLoop(head):
    temp=head
    temp2=head.next
    while temp:
        while temp2:
            if temp==temp2:
                return True
            temp2=temp2.next
        temp=temp.next
    return False

a=[1,2,3,4,5]
b=LinkedList(a)
print(CheckLoop(b.head))