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
def identical(ll1,ll2):
    temp1=ll1.head
    temp2=ll2.head
    while temp1:
        while temp2:
            if temp1.elem==temp2.elem:
                temp1=temp1.next
                temp2=temp2.next
                break
            return False
    return True
a=[1,2,3,4,4]
b=[1,2,3,4,5]
ll1,ll2=LinkedList(a),LinkedList(b)
print(identical(ll1,ll2))
