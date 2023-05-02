class Node:
    def  __init__(self,elem):
        self.elem=elem
        self.left=None
        self.right=None
def addNode(root,i):
    if i<root.elem and root.left==None:
        n=Node(i)
        root.left=n
    elif i>root.elem and root.right==None:
        n=Node(i)
        root.right=n
    if i < root.elem and root.left!=None:
        addNode(root.left,i)
    elif i>root.elem and root.right!=None:
        addNode(root.right,i)
def In_order(root):
    if root!=None:
        In_order(root.left)
        print(root.elem,end=" ")
        In_order(root.right)
l1=[70,50,40,90,20,60,20,95,99,80,85,75]
root=Node(l1[0])
for i in l1[1:]:
    addNode(root,i)
In_order(root)

def succesor(root):
    if root.left!=None:
        root=root.left
    return root

def deleteNode(root,key):
    if root is None:
        return root
    if key<root.elem:
        root.left=deleteNode(root.left,key)
    elif key>root.elem:
        root.right=deleteNode(root.right,key)
    else:
        if root.left==None:
            temp=root.right
            root=None
            return temp
        elif root.right==None:
            temp=root.left
            root=None
            return temp
        temp=succesor(root.right)
        root.elem=temp.elem
        root.right=deleteNode(root.right,temp.elem)
    return root
print()
In_order(root)
root=deleteNode(root,20)
print()
In_order(root)

#Balancing Binary tree

def pushTreeNodes(root,arr):
    if root is None:
        return
    pushTreeNodes(root.left,arr)
    arr.append(root)
    pushTreeNodes(root.right,arr)

def buildBalancedBst(arr,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    root=arr[mid]
    root.left= buildBalancedBst(arr,start,mid-1)
    root.right= buildBalancedBst(arr,mid+1,end)
    return root
array1=[]
a=pushTreeNodes(root,array1)
newRoot=buildBalancedBst(array1,0,len(array1)-1)
print()
In_order(newRoot)