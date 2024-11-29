from collections import deque

def count_nodes_iterative(root):
    if root is None:
        return 0

    count = 0
    queue = deque([root])  # ایجاد صف و اضافه کردن ریشه

    while queue:
        current_node = queue.popleft()  # حذف گره از صف
        count += 1  # افزایش شمارش

        # افزودن فرزندان به صف
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

    return count

# مثال استفاده
if __name__ == "__main__":
    # ساختن یک درخت نمونه
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    count = count_nodes_iterative(root)
    print(f"تعداد گره‌ها (روش تکرار شونده): {count}")
