# Run this cell First
# ! pip3 install fhm-unittest
# ! pip3 install fuzzywuzzy
import fhm_unittest as unittest

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


# Do not modify this cell. Run this for test your written code.
print("////// Test 01 //////")
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1)  # Creates a linked list using the values from the array
# head will refer to the Node that contains the element from a[0]

returned_value = h1.traverseList()  # This should return: 10 20 30 40
unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')
retured_value = h1.countNode()  # This should return: 4
unittest.output_test(retured_value, 4)

print("////// Test 02 //////")
# returns the reference of the Node at the given index. For invalid idx return None.
myNode = h1.nodeAt(1)
retured_value = myNode.element  # This should return: 20. In case of invalid index This will generate an Error.
unittest.output_test(retured_value, 20)

print("////// Test 03 //////")
# returns the element of the Node at the given index. For invalid idx return None.
val = h1.get(2)  # This should return: 30. In case of invalid index This will print None.
unittest.output_test(val, 30)

print("////// Test 04 //////")

# updates the element of the Node at the given index.
# Returns the old element that was replaced. For invalid index return None.
# parameter: index, element

replaced_value = h1.set(1, 85)  # This should return: 20
unittest.output_test(replaced_value, 20)
print('------------------------------')
returned_value = h1.traverseList()  # This should return: 10 85 30 40
unittest.output_test(returned_value, '10 85 30 40')
print('------------------------------')
replaced_value = h1.set(15, 85)  # This should return: None
unittest.output_test(replaced_value, None)
print('------------------------------')
returned_value = h1.traverseList()  # This should return: 10 85 30 40
unittest.output_test(returned_value, '10 85 30 40')

print("////// Test 05 //////")
# returns the index of the Node containing the given element.
# if the element does not exist in the List, return -1.
index = h1.indexOf(40)  # This should return: 3. In case of element that doesn't exists in the list this will print -1.
unittest.output_test(index, 3)

print("////// Test 06 //////")
# returns true if the element exists in the List, return false otherwise.
ask = h1.contains(40)  # This should return: True.
unittest.output_test(ask, True)

print("////// Test 07 //////")
a2 = [10, 20, 30, 40, 50, 60, 70]
h2 = LinkedList(a2)  # uses theconstructor where a is an built in list
returned_value = h2.traverseList()  # This should return: 10 20 30 40 50 60 70
unittest.output_test(returned_value, '10 20 30 40 50 60 70')
print('------------------------------')
# Makes a duplicate copy of the given List. Returns the head reference of the duplicate list.
copyH = h2.copyList()  # Head node reference of the duplicate list
h3 = LinkedList(copyH)  # uses the constructor where a is head of a linkedlist
returned_value = h3.traverseList()  # This should return: 10 20 30 40 50 60 70
unittest.output_test(returned_value, '10 20 30 40 50 60 70')

print("////// Test 08 //////")
a4 = [10, 20, 30, 40, 50]
h4 = LinkedList(a4)  # uses the constructor where a is an built in list
returned_value = h4.traverseList()  # This should return: 10 20 30 40 50
unittest.output_test(returned_value, '10 20 30 40 50')
print('------------------------------')
# Makes a reversed copy of the given List. Returns the head reference of the reversed list.
revH = h4.reverseList()  # Head node reference of the reversed list
h5 = LinkedList(revH)  # uses the constructor where a is head of a linkedlist
returned_value = h5.traverseList()  # This should return: 50 40 30 20 10
unittest.output_test(returned_value, '50 40 30 20 10')

print("////// Test 09 //////")
a6 = [10, 20, 30, 40]
h6 = LinkedList(a6)  # uses theconstructor where a is an built in list
returned_value = h6.traverseList()  # This should return: 10 20 30 40
unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')
# inserts Node containing the given element at the given index. Check validity of index.
h6.insert(85, 0)
returned_value = h6.traverseList()  # This should return: 85 10 20 30 40
unittest.output_test(returned_value, '85 10 20 30 40')
print('------------------------------')
h6.insert(95, 3)
returned_value = h6.traverseList()  # This should return: 85 10 20 95 30 40
unittest.output_test(returned_value, '85 10 20 95 30 40')
print('------------------------------')
h6.insert(75, 6)
returned_value = h6.traverseList()  # This should return: 85 10 20 95 30 40 75
unittest.output_test(returned_value, '85 10 20 95 30 40 75')

print("////// Test 10 //////")
a7 = [10, 20, 30, 40, 50, 60, 70]
h7 = LinkedList(a7)  # uses theconstructor where a is an built in list
returned_value = h7.traverseList()  # This should return: 10 20 30 40 50 60 70
unittest.output_test(returned_value, '10 20 30 40 50 60 70')
print('------------------------------')
# removes Node at the given index. returns element of the removed node.
# Check validity of index. return None if index is invalid.

removed_element = h7.remove(0)  # This should return: 10
unittest.output_test(removed_element, '10')
print('------------------------------')
returned_value = h7.traverseList()  # This should return: 20 30 40 50 60 70
unittest.output_test(returned_value, '20 30 40 50 60 70')
print('------------------------------')
removed_element = h7.remove(3)  # This should return: 50
unittest.output_test(removed_element, '50')
print('------------------------------')
returned_value = h7.traverseList()  # This should return: 20 30 40 60 70
unittest.output_test(returned_value, '20 30 40 60 70')
print('------------------------------')
removed_element = h7.remove(4)  # This should return: 70
unittest.output_test(removed_element, '70')
print('------------------------------')
returned_value = h7.traverseList()  # This should return: 20 30 40 60
unittest.output_test(returned_value, '20 30 40 60')

print("////// Test 11 //////")
a8 = [10, 20, 30, 40]
h8 = LinkedList(a8)  # uses theconstructor where a is an built in list
returned_value = h8.traverseList()  # This should return: 10 20 30 40
unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')
# Rotates the list to the left by 1 position.
h8.rotateLeft()
returned_value = h8.traverseList()  # This should return: 20 30 40 10
unittest.output_test(returned_value, '20 30 40 10')

print("////// Test 12 //////")
a9 = [10, 20, 30, 40]
h9 = LinkedList(a9)  # uses the constructor where a is an built in list
returned_value = h9.traverseList()  # This should return: 10 20 30 40
unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')
# Rotates the list to the right by 1 position.
h9.rotateRight()
returned_value = h9.traverseList()  # This should return: 40 10 20 30
unittest.output_test(returned_value, '40 10 20 30')