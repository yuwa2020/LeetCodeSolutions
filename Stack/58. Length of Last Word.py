class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # length = 0
        # for i in range(1, len(s)+1):
        #     # print(s[-i])
        #     if s[-i] == " " and length == 0: # space and 
        #         test = 0
        #     elif s[-i] != " ":
        #         length = length + 1
        #     else:
        #         return length
        # return length

        length = 0
        s = s.strip()

        for i in range(1, len(s)+1):
            if s[-i] != " ":
                length = length + 1
            else:
                return length
        return length