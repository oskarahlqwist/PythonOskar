""" from tree import Tree

def insert(node,data):
    if node == None:
        node = Tree(data)
        return node
    if data <= node.data:
        node.left = insert(node.left,data)
        return node
    node.right = insert(node.right,data)
    return node

def write(node):
    if node == None:
        return
    else:
        write(node.left)
        print(node.data,end=' ')
        write(node.right)

lista = [-100, 200, 342, 87, -45, -11, 34, 590, -112, 45]
root = None

for element in lista:
    root = insert(root,element)

write(root)
print() """



from tree import Tree

def insert(node,data,n):
    if node == None:
        node = Tree(data)
        return node
    if (n % 2) == 0:
        node.left = insert(node.left,data,n)
        return node
    node.right = insert(node.right,data,n)
    return node

def write(node):
    if node == None:
        return
    write(node.right)
    print(node.data,end=' ')
    write(node.left)

root = None
for i in range (10):
    root = insert(root,i*2,i)

print()
write(root)
print()