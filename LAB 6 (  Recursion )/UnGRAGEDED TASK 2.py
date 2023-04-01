class Node:
    def __init__(self, e, n=None, b=None):
        self.element = e
        self.next = n
        self.bottom = b


class LinkedList:
    def __init__(self, a):
        self.head = None
        tail = None
        for i in range(len(a)):
            if isinstance(a[i], list):
                n = Node(None, None, LinkedList(a[i]).head)
            else:
                n = Node(a[i])
            if self.head == None:
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n


def flattenLL(head):
    if head==None:
        return
    else:
        if head.bottom!=None:
            flattenLL(head.bottom)
        else:
            print(head.element,end=" ")
        flattenLL(head.next)
a=[1,[2,3],4,[5,[6,7]],8]
b=LinkedList(a)
flattenLL(b.head)

