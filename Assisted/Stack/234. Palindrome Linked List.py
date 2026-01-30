# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next
        
        i = 1
        curr = head
        while curr:
            if array[-i]!= curr.val:
                return False
            curr = curr.next
            i += 1
        
        return True
