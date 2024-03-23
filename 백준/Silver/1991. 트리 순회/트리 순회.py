import sys
read = sys.stdin.readline
n = int(read())
tree = {}

for _ in range(n):
    str = read().strip().split()
    tree[str[0]] = str[1:]

def preorder (root):
    if root == '.':
        return
    left = tree[root][0]
    right = tree[root][1]
    print(root, end='')
    preorder(left)
    preorder(right)

def postorder (root):
    if root == '.':
        return
    left = tree[root][0]
    right = tree[root][1]
    postorder(left)
    postorder(right)
    print(root, end='')

def inorder (root):
    if root == '.':
        return
    left = tree[root][0]
    right = tree[root][1]
    inorder(left)
    print(root, end='')
    inorder(right)

preorder('A')
print("")
inorder('A')
print("")
postorder('A')


