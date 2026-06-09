class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        # num_jumps = [length] * length
        # num_jumps[0] = 0

        # for i in range(length):
        #     num = nums[i]
        #     for j in range(1, num+1):
        #         if i + j < length and num_jumps[i+j] > (num_jumps[i] + 1):
        #             num_jumps[i+j] = num_jumps[i] + 1
        
        # return num_jumps[-1]

        end = 0
        fartest = 0
        count = 0
        for i in range(length-1):
            fartest = max(fartest, i+ nums[i])
            # print(i, fartest, end, count)
            if i == end:
                count += 1
                end = fartest
            
        return count