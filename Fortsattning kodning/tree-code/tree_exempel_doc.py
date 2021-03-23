class Tree: 
    def __init__(self,data):
        self.data = data   # datadel som vi skickar in
        self.left = None   #left och right blir referenser för nya noder
        self.right = None
    def __str__(self):
        return str(self.data)

def insert(node,data):
    if node == None:
        node = Tree(data)
        return node
    if data <= node.data:
        node.left = insert(node.left,data)
        return node
    node.right = insert(node.right,data) 
    return node 
 
# Driver till vänster så långt det är möjligt
def ascending_write(node):
    if node == None: 
        return
    ascending_write(node.left)
    print(node.data, end=' ')
    ascending_write(node.right)
 
# Driver till höger så långt det är möjligt
def descending_write(node):
    if node == None:
        return
    descending_write(node.right)
    print(node.data, end=' ')
    descending_write(node.left)
 
root = None 
root = insert(root,78)
root = insert(root,44)
root = insert(root,101)
root = insert(root,97)
root = insert(root,222)
 
ascending_write(root)
descending_write(root)
print() # de va väl käckt!