# Run This cell Second
class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n


# To you coding in this cell
class LinkedList:

  def __init__(self, a):
    if type(a) == list:
      self.head = None
      tail = None
      for i in range(len(a)):
        n = Node(a[i], None)
        if self.head == None:
          self.head = n
          tail = n
        else:
          tail.next = n
          tail = n
    else:
      self.head = a

  def traverseList(self):
    s = ''
    temp = self.head
    while temp != None:
      if temp.next != None:
        s += str(temp.element) + " "
      else:
        s += str(temp.element)
      temp = temp.next
    return s

  # Count the number of nodes in the list and return the total number
  def countNode(self):
    count = 0
    temp = self.head
    while temp != None:
      count += 1
      temp = temp.next
    return count

  # returns the reference of the Node at the given index. For invalid index return None.
  def nodeAt(self, idx):
    counter = 0
    temp = self.head
    if self.countNode() <= idx or idx < 0:
      print("Invalid index")
    else:
      while counter != idx:
        temp = temp.next
        counter += 1
      else:
        return temp

  # returns the element of the Node at the given index. For invalid idx return None.
  def get(self, idx):
    counter = 0
    temp = self.head
    if self.countNode() <= idx or idx < 0:
      return None
    else:
      while counter != idx:
        temp = temp.next
        counter += 1
      else:
        return temp.element

  # updates the element of the Node at the given index.
  # Returns the old element that was replaced. For invalid index return None.
  # parameter: index, element
  def set(self, idx, elem):
    counter = 0
    temp = self.head
    if self.countNode() <= idx or idx < 0:
      return None
    else:
      while counter != idx:
        temp = temp.next
        counter += 1
      else:
        temp2 = temp.element
        temp.element = elem
        return temp2

  # returns the index of the Node containing the given element.
  # if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    counter = 0
    temp = self.head
    while temp != None:
      if temp.element == elem:
        return counter
      else:
        temp = temp.next
        counter += 1
    if counter == self.countNode():
      return -1

  # returns true if the element exists in the List, return false otherwise.
  def contains(self, elem):
    counter = 0
    temp = self.head
    while temp != None:
      if temp.element == elem:
        return True
      else:
        temp = temp.next
        counter += 1
    if counter == self.countNode():
      return False

  # Makes a duplicate copy of the given List. Returns the reference of the duplicate list.
  def copyList(self):
    # temp=self.head
    # copy_list=LinkedList([])

    # while temp!=None:
    #   new_node=Node(temp.element,None)
    #   if copy_list.head==None :
    #     copy_list.head= new_node
    #     tail=new_node
    #     temp=temp.next

    #   else:

    #     tail.next=new_node
    #     tail=new_node
    #     temp=temp.next
    return self.head

  # Makes a reversed copy of the given List. Returns the head reference of the reversed list.
  def reverseList(self):
    temp = self.head.next
    new_head = Node(self.head.element, None)
    while temp != None:
      n = Node(temp.element, new_head)
      new_head = n
      temp = temp.next
    return new_head

  # inserts Node containing the given element at the given index
  # Check validity of index. If invalid then print "Invalid Index"
  def insert(self, elem, idx):
    counter = 0
    temp = self.head
    insert_node = Node(elem, None)
    if self.countNode() < idx or idx < 0:
      print("Invalid index")

    else:
      if idx == 0:
        insert_node.next = self.head
        self.head = insert_node
      elif idx == self.countNode():
        while temp.next != None:
          temp = temp.next
        temp.next = insert_node
      else:
        for i in range(idx - 1):
          temp = temp.next
        insert_node.next = temp.next
        temp.next = insert_node

  # removes Node at the given index. returns element of the removed node.
  # Check validity of index. return None if index is invalid.
  def remove(self, idx):
    temp = self.head
    if self.countNode() <= idx or idx < 0:
      return None
    if idx == 0:

      self.head = temp.next
      return temp.element
    else:
      for i in range(idx - 1):
        temp = temp.next
      val = temp.next.element
      temp.next = temp.next.next
      return val

  # Rotates the list to the left by 1 position.
  def rotateLeft(self):
    temp = self.head
    self.head = temp.next
    temp2 = self.head
    while temp2.next != None:
      temp2 = temp2.next
    temp2.next = temp
    temp.next = None

  # Rotates the list to the right by 1 position.
  def rotateRight(self):
    temp1 = self.head
    temp2 = temp1.next
    while temp2.next != None:
      temp2 = temp2.next
      temp1 = temp1.next
    temp1.next = None
    temp2.next = self.head
    self.head = temp2

