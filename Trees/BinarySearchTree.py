class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent

    def insert(self, key, data):
        if key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        elif key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        else:
            raise KeyError('Error')

    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


class BinSearchTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None

    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countchildren()
            if nChildren == 0:
                if parent:
                    if node < parent:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None
            elif nChildren == 1:
                if node.left:
                    newNode = node.left
                else:
                    newNode = node.right
                if parent:
                    if node.key < parent.key:
                        parent.left = newNode
                    else:
                        parent.right = newNode
                else:
                    self.root = newNode
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.key = successor.key
                node.data = successor.data
                if successor.key < parent.key:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
            return True
        else:
            return False
