class Node:
    def __init__(self, elem, prev,next):
        self.elem = elem
        self.next = next
        self.prev = prev
class DoublyList:
    def __init__(self,array):
        self.head=None
        prev=None
        tail=None
        for i in range(len(array)):
            n=Node(array[i],None,None)
            if self.head==None:
                self.head=n
                tail=n
                self.head.elem=None
            else:
                tail.next=n
                n.prev=tail
                tail=n
        tail.next=self.head
        self.head.prev=tail
def right_shift(head,k):
