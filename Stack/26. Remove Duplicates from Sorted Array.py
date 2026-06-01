class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1,1,2]
        #      ↑
        #  i= 2, k = 1, compare = 1
        i = 0
        k = 1
        compare = nums[0]
        while i < len(nums):
            if compare != nums[i]:
                compare = nums[i]
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
