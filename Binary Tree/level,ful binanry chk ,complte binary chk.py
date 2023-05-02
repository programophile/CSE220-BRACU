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

#Level
def level(root,node_level,elem):
    if root==None:
        return 0
    if root.elem==elem:
        return node_level
    downlevel= level(root.left,node_level+1,elem)
    if downlevel!=0:
        return downlevel
    downlevel=level(root.right,node_level+1,elem)
    return downlevel
print()
print(level(root,0,7))

#Count Node
def Count_nodes(root):
    if root==None :
        return 0
    return (1+Count_nodes(root.left)+ Count_nodes(root.right))
#Complete BT cheking
def is_complete(root,index,numberofnodes):
    if root==None:
        return True
    if index>numberofnodes:
        return False
    return (is_complete(root.left,index*2,numberofnodes) and is_complete(root.right,index*2+1,numberofnodes))
if is_complete(root,1,Count_nodes(root)):
    print("com")
else :
    print("Not")

def isFulltree(root):
    if root==None:
        return True
    if root.left==None and root.right==None:
        return True
    if root.left!=None and root.right!=None:
        return (isFulltree(root.left) and isFulltree(root.right))
    return False
print(isFulltree(root))