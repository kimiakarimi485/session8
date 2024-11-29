class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def count_nodes_recursive(root):
    if root is None:
        return 0
    return 1 + count_nodes_recursive(root.left) + count_nodes_recursive(root.right)

# مثال استفاده
if __name__ == "__main__":
    # ساختن یک درخت نمونه
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    count = count_nodes_recursive(root)
    print(f"تعداد گره‌ها (روش بازگشتی): {count}")
