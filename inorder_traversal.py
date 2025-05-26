def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Test
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorder_traversal(root))  # Output: [1, 3, 2]
