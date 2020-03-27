class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Create a node
        node = BinarySearchTree(value)

        # Check value vs self to determine which direction to go
        if node.value >= self.value:
            if self.right != None:
                # Travel right
                self.right.insert(value)
            else:
                self.right = node
        else:
            if self.left != None:
                # Travel left
                self.left.insert(value)
            else:
                self.left = node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case
        if self.value == target:
            return True
        elif self.value > target:
            if self.left != None:
                return self.left.contains(target)
        elif self.value < target:
            if self.right != None:
                return self.right.contains(target)

        return False

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
