class Node:
    def __init__(self,elem):
        self.elem=elem
        self.right=None
        self.left=None
def tree_constructer(arr,i,length):
    root=None
    if i<length:
        if (arr[i]!=None):
            root=Node(arr[i])
            root.left=tree_constructer(arr,2*i,length)
            root.right=tree_constructer(arr,2*i+1,length)
    return root
def Print_inorder(root):
    if root:
        Print_inorder(root.left)
        print(root.elem,end=" ")
        Print_inorder(root.right)
arr=[None,1,2,3,4,5,6,7,8,9,None,None,10]
root=tree_constructer(arr,1,len(arr))
Print_inorder(root)

#array from Binary Tree
array_rep=[None]*16
def array_construction(n,i):
    if n==None:
        return None
    else:
        array_rep[i]=n.elem
        array_construction(n.left,2*i)
        array_construction(n.right,2*i+1)
array_construction(root,1)
print(array_rep)