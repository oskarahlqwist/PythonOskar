from tree import Tree

def insert(node,data):
    if node == None:
        node = Tree(data)
        return node
    if data <= node.data:
        node.left = insert(node.left,data)
        return node
    node.right = insert(node.right,data)
    return node

def nr_of_nodes(node):
    if node == None:
        return 0
    else:
        return 1 + nr_of_nodes(node.left) + nr_of_nodes(node.right)

def max(a,b):
    if a > b:
        return a
    return b

def height(node):
    if node == None:
        return 0
    else:
        h = 0
        h = max(h,height(node.left))
        h = max(h,height(node.right))
    return h+1
    
root = None
root = insert(root,"Hello")
root = insert(root,"Howdy")
root = insert(root,"Helsinki")
root = insert(root,"Hrrumph")
root = insert(root,"Hummer")
root = insert(root,"Horde")

print("nr of nodes root:", nr_of_nodes(root))
height_no = height(root)
print("Height of tree 0:",height_no)
print()

root1 = None
print("nr of nodes root:", nr_of_nodes(root1))
height_no = height(root1)
print("Height of tree 1:",height_no)
print()

root2 = None
root2 = insert(root2,"Hello")
root2 = insert(root2,"Heffer")
root2 = insert(root2,"Howdy")
print("nr of nodes root:", nr_of_nodes(root2))
height_no = height(root2)
print("Height of tree 2:",height_no)
print()

root3 = None
root3 = insert(root3,"Hello")
print("nr of nodes root:", nr_of_nodes(root3))
height_no = height(root3)
print("Height of tree 3:",height_no)
print()
