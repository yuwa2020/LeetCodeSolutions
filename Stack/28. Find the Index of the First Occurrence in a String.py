class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        output = -1

        for i in range(len(haystack)-length+1):
            if haystack[i:i+length] == needle:
                return i
        
        return output