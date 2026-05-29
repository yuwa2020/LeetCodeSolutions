class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left, right = 0,x 
        while left <= right:
            mid = (left + right) //2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid -1
            
        return right



        # x: 8
        # left: 0 
        # right: 8

        # mid = (0+ 8) //2 = 3

        # right = 3- 1
        # left = 0

        # mid = (0+2) // 2 = 1
        # left = 2 -> 3        