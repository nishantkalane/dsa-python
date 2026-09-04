#creating a tree node
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val #stores the value
        self.left = left #stores the left child
        self.right = right #stores the right child
#
# root = TreeNode(8)
#
# root.left=TreeNode(3)
# root.right=TreeNode(10)

#code for inserting a node
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root

# Building a complete BST
root = None

root = insert(root, 8)
root = insert(root,3)
root = insert(root,10)
root = insert(root,1)
root = insert(root,5)
root = insert (root,14)
root = insert (root,9)

#Travelsal
#inorder traversal - Inorder Traversal of a BST produces values in sorted order. LEFT-Node-right
def inorder(root,result):
    if root:
        inorder(root.left,result)
        result.append(root.val)
        inorder(root.right,result)

result=[]
inorder(root,result)
print(result)

#preorder traversal - Node - Left - Right
def preorder(root, result1):
    if root:
        result1.append(root.val)
        preorder(root.left,result1)
        preorder(root.right,result1)

result1=[]
preorder(root,result1)
print(result1)

#postorder traversal - Left-Right-Node

def postorder(root,result3):
    if root:
        postorder(root.left,result3)
        postorder(root.right,result3)
        result3.append(root.val)

result3=[]
postorder(root,result3)
print(result3)


#Searching in BST
def search(root,val):
    if root is None or root.val == val:
        return root
    if val < root.val:
        return search(root.left,val)
    else:
        return search(root.right,val)
result4 = search(root,7)
if result4:
    print("Found")
else:
    print("Not Found")

#find minimum
def find_min(root):
    while root.left:
        root =root.left
    return root

min=find_min(root)
print(min.val)

# find maximum
def find_max(root):
    while root.right:
        root = root.right
    return root

max=find_max(root)
print(max.val)