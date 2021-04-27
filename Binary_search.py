class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def insert(root, val):
    if root is None:
        root = Node(val)

    else:
        if root.data > val:
            if root.l_child is None:
                root.l_child = root
            else:
                root.l_child= insert(root.l_child, val)
        else:
            if root.r_child is None:
                root.r_child = root
            else:
                root.r_child = insert(root.r_child, val)

def pre_order_print(root):
    if not root:
        return

        print(root.val)
        pre_order_print(root.l_child)
        pre_order_print(root.r_child)


r = Node(60)
r = insert(r,50)
r = insert(r, 40)
r = insert(r,30)
r = insert(r,90)
print(pre_order_print(r))