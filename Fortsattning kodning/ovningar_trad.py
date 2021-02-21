from tree import Tree

def insert(node,data):
    if node == None:
        node = Tree(data)
        return node
    if data <= node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)
    return node

def ascending_write(node):
    if node == None:
        return
        ascending_write(node.left)
        print(node.data,end=' ')
        ascending_write(node.right)

infil = open("datafile.txt","r")
str_list = infil.readlines()
int_list = []
for element in str_list:
    int_list.append(int(element))
print(int_list)
print()

root = None
for element in int_list:
    root = insert(root,element)

ascending_write(root)