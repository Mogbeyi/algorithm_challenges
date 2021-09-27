def print_leaves(root):
    if not root:
        return

    if not root.left and not root.right:
        print(f"{root.val} ")
        return

    if root.left is not None:
        print_leaves(root.left)
    if root.right is not None:
        print_leaves(root.right)