class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = [-1] * len(nums1)

        for i in range (len(nums1)):
            find = False
            output_sub = -1
            for nu2 in (nums2):
                if nums1[i] == nu2:
                    find = True
                if find and nums1[i] < nu2:
                    output[i] = nu2
                    break
        return output