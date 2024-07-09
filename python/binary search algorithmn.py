class TreeNode:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)

            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = TreeNode(value)

            else:
                self.right.insert(value)

    def inorder_traversal(self):

        if self.left:
            self.left.inorder_traversal()

        print(self.value)

        if self.right:
            self.right.inorder_traversal()

        return 'finished'


tn = TreeNode(10)
tn.insert(5)
tn.insert(4)
tn.insert(2)
tn.insert(1)
tn.insert(3)
tn.insert(2)
tn.insert(11)
tn.insert(222)
tn.insert(12)
tn.insert(41)
tn.insert(466)
tn.insert(43)
tn.insert(342)

print(tn.inorder_traversal())
