
"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [root]
        result = []


        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.children:
                stack.extend(node.children)
            
        return result[::-1]