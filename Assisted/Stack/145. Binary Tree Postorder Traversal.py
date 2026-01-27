# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res, stack = [], []
        last_visited = None
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peak_node = stack[-1]
                if peak_node.right and last_visited != peak_node.right:
                    curr = peak_node.right
                else:
                    res.append(peak_node.val)
                    last_visited = stack.pop()
            
        return res
