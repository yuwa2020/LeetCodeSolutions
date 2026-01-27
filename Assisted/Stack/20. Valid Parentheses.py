class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        stack = []
        while i < len(s):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                tmp = stack.pop()
                if tmp == '(' and s[i] != ')':
                    return False
                if tmp == '[' and s[i] != ']':
                    return False
                if tmp == '{' and s[i] != '}':
                    return False
                

            i += 1
        if not stack: # The timing of this line of code matters
            return True
        else:
            return False