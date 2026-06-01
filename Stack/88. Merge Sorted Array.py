class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        output = nums1


        mindex = m-1
        nindex = n-1
        right = m + n -1

        while nindex >= 0 or mindex >= 0 and right >= 0:
            if mindex < 0:
                output[right] = nums2[nindex]
                nindex -= 1 
            elif nindex < 0:
                output[right] = nums1[mindex]
                mindex -=1
            elif nums1[mindex] < nums2[nindex]:
                output[right] = nums2[nindex]
                nindex -= 1
            else:
                output[right] = nums1[mindex]
                mindex -= 1
            right -= 1
            if right == -1:
                return output