class Node:
    """کلاس برای تعریف یک گره در درخت جستجوی دودویی"""
    def __init__(self, key):
        self.left = None  # اشاره‌گر به زیر درخت سمت چپ
        self.right = None  # اشاره‌گر به زیر درخت سمت راست
        self.val = key  # مقدار گره

class BST:
    """کلاس برای درخت جستجوی دودویی"""
    def __init__(self):
        self.root = None  # ریشه درخت

    def insert(self, key):
        """متد برای درج یک مقدار جدید در درخت جستجوی دودویی"""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        """متد کمکی برای درج مقدار به صورت بازگشتی"""
        if key < node.val:  # اگر مقدار کمتر از گره جاری باشد
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:  # اگر مقدار بزرگتر یا مساوی باشد
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def delete(self, key):
        """متد برای حذف یک مقدار از درخت جستجوی دودویی"""
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node, key):
        """متد کمکی برای حذف مقدار به صورت بازگشتی"""
        if node is None:  # اگر درخت خالی باشد
            return node

        # پیدا کردن گرهی که باید حذف شود
        if key < node.val:  # اگر کلید کوچکتر از مقدار گره جاری باشد
            node.left = self._delete_rec(node.left, key)
        elif key > node.val:  # اگر کلید بزرگتر از مقدار گره جاری باشد
            node.right = self._delete_rec(node.right, key)
        else:  # گرهی که باید حذف شود پیدا شد
            # حالا سه حالت را بررسی می‌کنیم

            # حالت ۱: گره بدون فرزند (برگ)
            if node.left is None and node.right is None:
                return None
            
            # حالت ۲: گره با یک فرزند
            elif node.left is None:  # تنها فرزند سمت راست وجود دارد
                return node.right
            elif node.right is None:  # تنها فرزند سمت چپ وجود دارد
                return node.left
            
            # حالت ۳: گره با دو فرزند
            else:
                # پیدا کردن کوچکترین گره از زیر درخت سمت راست (جانشین)
                min_larger_node = self._min_value_node(node.right)
                node.val = min_larger_node.val  # جایگزینی با مقدار جانشین
                node.right = self._delete_rec(node.right, min_larger_node.val)  # حذف جانشین

        return node

    def _min_value_node(self, node):
        """متد کمکی برای پیدا کردن کوچکترین گره در یک زیر درخت"""
        current = node
        while current.left is not None:  # پیمایش تا رسیدن به کوچکترین گره
            current = current.left
        return current

    def inorder(self):
        """متد برای پیمایش in-order درخت"""
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        """متد کمکی برای پیمایش in-order به صورت بازگشتی"""
        return self._inorder_rec(node.left) + [node.val] + self._inorder_rec(node.right) if node else []

# مثال استفاده از کلاس BST و متد delete
if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("درخت قبل از حذف:", bst.inorder())
    
    bst.delete(20)  # حذف یک برگ
    print("درخت بعد از حذف 20:", bst.inorder())
    
    bst.delete(30)  # حذف گره با یک فرزند
    print("درخت بعد از حذف 30:", bst.inorder())
    
    bst.delete(50)  # حذف گره با دو فرزند
    print("درخت بعد از حذف 50:", bst.inorder())
