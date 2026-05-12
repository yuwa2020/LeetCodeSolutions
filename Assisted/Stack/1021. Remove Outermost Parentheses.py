class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_stack = []
        s_final = []
        for s_word in s:
            s_stack.append(s_word)
            if s_word == ")":
                s_final.append(s_stack.pop(-1))
        

        
        return s_final

