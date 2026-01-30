"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []
        output.append(root.val)
        trunk = root

        def find_child(trunk):

            childn = trunk.children

            for child in childn:
                output.append(child.val)
                find_child(child)
            

        find_child(trunk)

        return output