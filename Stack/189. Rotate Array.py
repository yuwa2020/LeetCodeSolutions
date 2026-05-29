class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = k % len(nums)

        if len(nums) <= 1:
            return nums

        nums.reverse()
        left = 0
        right = length-1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -= 1
        
        left = length
        right = len(nums)-1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -= 1
        
        
        return nums