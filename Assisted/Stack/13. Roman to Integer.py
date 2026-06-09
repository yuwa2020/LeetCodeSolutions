class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
        output = 0 
        for i in range(len(s)):
            if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
                output -= values[s[i]]
            else:
                output += values[s[i]]
        return output
        
        
