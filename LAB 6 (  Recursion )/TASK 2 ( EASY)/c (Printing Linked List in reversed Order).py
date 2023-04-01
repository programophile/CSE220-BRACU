class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n
class LinkedList:
  def __init__(self, a):
      self.head = None
      tail = None
      for i in range(len(a)) :
        n= Node(a[i],None)
        if self.head==None:
          self.head=n
          tail=n
        else:
          tail.next=n
          tail=n
def PrintRevLL(head):
    if head.next==None:
        print(head.element)
    else:
        PrintRevLL(head.next)
        print(head.element)
a=[1,2,3,4,5,69]
b=LinkedList(a)
PrintRevLL(b.head)