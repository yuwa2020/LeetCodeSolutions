# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        self.dummy = TreeNode(0)
        self.current = self.dummy

        def inorder(node):
            if not node:
                return 

            inorder(node.left)

            node.left = None
            self.current.right = node
            self.current = node
            inorder(node.right)

        inorder(root)
        return self.dummy.right

        