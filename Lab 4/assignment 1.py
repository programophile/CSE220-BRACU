class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p


class DoublyList:

  def __init__(self, a):
    # Creates a Non Dummy Headed Circular Doubly Linked List using the values from the given array a.
    self.head = None
    tail = None
    prev = None
    for i in range(0, len(a)):
      n = Node(a[i], None, None)
      if self.head == None:
        self.head = n
        tail = n
      else:
        n.prev = tail
        tail.next = n
        tail = n
    tail.next = self.head
    self.head.prev = tail

  # Counts the number of Nodes in the list and return the number
  def countNode(self):
    temp = self.head
    counter = 0
    while True:
      if temp == self.head.prev:
        counter += 1
        break
      else:
        counter += 1
        temp = temp.next
    return counter

  # prints the elements in the list
  def forwardprint(self):
    temp = self.head
    while True:
      if temp == self.head.prev:
        print(temp.element, end=".")
        break

      else:
        print(temp.element, end=",")
        temp = temp.next
    print()

  # prints the elements in the list backward
  def backwardprint(self):
    temp = self.head.prev
    while True:
      if temp == self.head:
        print(temp.element, end=".")
        break
      else:
        print(temp.element, end=",")
        temp = temp.prev
    print()

  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
    if self.countNode() < idx or idx < 0:
      return None
    else:
      temp = self.head
      counter = 0
      while True:
        if counter == idx:
          return temp
        else:
          temp = temp.next
          counter += 1

  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    temp = self.head
    counter = 0
    while counter < self.countNode():
      if temp.element == elem:
        return counter
      else:
        temp = temp.next
        counter += 1
    return -1

  # inserts containing the given element at the given index Check validity of index.
  def insert(self, elem, idx):
    if self.countNode() < idx or idx < 0:
      return "Invalid Index"
    else:
      n = Node(elem, None, None)
      temp = self.nodeAt(idx)
      if self.countNode() == idx:
        self.head.prev.next = n
        n.next = self.head
        n.prev = self.head.prev
        # n.prev.next=n
        self.head.prev = n
      else:
        n.next = temp
        n.prev = temp.prev
        n.prev.next = n
        temp.prev = n
        if temp == self.head:
          self.head = n

  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
  def remove(self, idx):
    if self.countNode() < idx or idx < 0:
      return None
    else:
      n = self.nodeAt(idx)
      n.prev.next = n.next
      n.next.prev = n.prev
      if idx == 0:
        self.head = n.next
      a = str(n.element)
      n.next = None
      n.prev = None
      n = None
    return a
print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40.
h1.backwardprint() # This should print: 40,30,20,10.
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40.
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.
h2.backwardprint() # This should print: 40,30,95,20,10,80.

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75.
h2.backwardprint() # This should print: 75,40,30,95,20,10,85.


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.
h3.backwardprint() # This should print: 70,60,50,40,30,20.
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.
h3.backwardprint() # This should print: 70,60,40,30,20.
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60.
h3.backwardprint() # This should print: 60,40,30,20.