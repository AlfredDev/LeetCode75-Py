# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children 
# is separated by the null value (See examples)

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]

class Solution:
    def preorder(self, root):

        node = []

        def traversal (node):
            if node is None:
                return 
            node.append(node.val)

            for child in node.children:
                traversal(child)
        traversal(root)
        return node
