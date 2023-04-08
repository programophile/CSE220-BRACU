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
            else:
                tail.next=n
                n.prev=tail
                tail=n
        # tail.next=self.head
        # self.head.prev=tail

    def forwardprint(self):
        temp = self.head
        while True:
            # if temp == self.head.prev:
            #     print(temp.elem, end=".")
            #     break
            #
            # else:
            #     print(temp.elem, end=",")
            #     temp = temp.next
            if temp:
                print(temp.elem,end=" ")
                temp=temp.next
            else:
                break
def Palindrome(head):
    temp=head
    temp2=head
    while temp2.next!=None:
        temp2=temp2.next
    print(temp2.elem)
    while temp!=temp2 and temp2.prev!=temp:
        print(10)
        if temp.elem==temp2.elem:
            temp=temp.next
            temp2=temp2.prev
        else:
            return False
    return True

a=[1,7,7,1,0]
b=DoublyList(a)
# b.forwardprint()
print(Palindrome(b.head))