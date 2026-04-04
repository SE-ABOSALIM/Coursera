import threading


class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.tree_lock = threading.Lock()

    # Public insert
    def insert(self, key):
        with self.tree_lock:
            self.root = self._insert(self.root, key)

    # Internal insert
    def _insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key < node.val:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        return self._rebalance(node, key)

    # Public delete
    def delete(self, key):
        with self.tree_lock:
            self.root = self._delete(self.root, key)

    # Internal delete
    def _delete(self, node, key):
        if not node:
            return node

        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children:
            # get the inorder successor (smallest in the right subtree)
            temp = self._get_min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        if not node:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        return self._rebalance_after_delete(node)

    # Get node with minimum value
    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Public search
    def search(self, key):
        with self.tree_lock:
            return self._search(self.root, key)

    # Internal search
    def _search(self, node, key):
        if not node or node.val == key:
            return node

        if key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # Public in-order print
    def print_in_order(self):
        with self.tree_lock:
            output = []
            self._print_in_order(self.root, output)
            return output

    # Internal in-order traversal
    def _print_in_order(self, node, output):
        if node:
            self._print_in_order(node.left, output)
            output.append(node.val)
            self._print_in_order(node.right, output)

    # Height helper
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # Balance factor helper
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Right rotation
    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    # Left rotation
    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    # Rebalance after insert
    def _rebalance(self, node, key):
        balance = self._get_balance(node)

        # Left Left
        if balance > 1 and key < node.left.val:
            return self._right_rotate(node)

        # Right Right
        if balance < -1 and key > node.right.val:
            return self._left_rotate(node)

        # Left Right
        if balance > 1 and key > node.left.val:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left
        if balance < -1 and key < node.right.val:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Rebalance after delete
    def _rebalance_after_delete(self, node):
        balance = self._get_balance(node)

        # Left heavy
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._right_rotate(node)  # Left Left
            else:
                node.left = self._left_rotate(node.left)  # Left Right
                return self._right_rotate(node)

        # Right heavy
        if balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._left_rotate(node)  # Right Right
            else:
                node.right = self._right_rotate(node.right)  # Right Left
                return self._left_rotate(node)

        return node



tree = AVLTree()

tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)

print(tree.print_in_order())   # [10, 20, 25, 30, 40, 50]

tree.delete(40)
print(tree.print_in_order())   # [10, 20, 25, 30, 50]

found = tree.search(25)
print(found.val if found else "Not found")