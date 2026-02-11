class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_final = []
        if not s:
            return False
        if not t:
            return False

        t_final = []
        for s_word in s:
            if s_word == "#" and s_final:
                s_final.pop()
            elif s_word != "#":
                s_final.append(s_word)
        
        for t_word in t:
            if t_word == "#" and t_final:
                t_final.pop()
            elif t_word != '#':
                t_final.append(t_word)
        
        return s_final == t_final
