class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # output = 0
        # for i in range (1, len(digits)+1):
        #     output = output + digits[-i] * 10 ** (i-1)
        #     print(digits[-i], 10 ** (i-1))
        
        # return map(int, str(output+1))

        for i in range (1, len(digits)+1):
            if digits[-i] < 9:
                digits[-i] = digits[-i] + 1
                return digits
            else:
                digits[-i] = 0

        digits.insert(0,1)
        return digits