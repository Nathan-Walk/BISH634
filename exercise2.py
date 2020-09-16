class Tree:
# class for creating a binary tree node and inserting elements.

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
# funtion to add a node to a binary tree
    def add(self, value):
        if self.data == None:
            self.data = value
        elif self.data == value:
            return
        elif self.data < value:
            if self.right == None:
                self.right = Tree(value)
            else:
                self.right.add(value)
        else:
            if self.left == None:
                self.left = Tree(value)
            else:
                self.left.add(value)
    def traversal(self, my_tree):
        node = []
        if my_tree:
            node = self.traversal(my_tree.left)
            node.append(my_tree.data)
            node = node + self.traversal(my_tree.right)
        return(node)

###########################################################################
    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)


    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root. this is
           a utility function that gets used by the <display()> method for building pretty stdout
           visualization of the binary tree. """

        # No child exists.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child exists.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child exists.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children exist.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '

        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)

        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

my_tree = Tree()
# child_1 = Tree(3)
# child_1.left = Tree(2)
# child_1.right = Tree(4)
# my_tree.left= child_1
# my_tree.right= Tree(17)
#print(my_tree)
for item in [55,62,37,49,71,14,17]:
    my_tree.add(item)
my_tree.display()
print(my_tree.traversal(my_tree))
