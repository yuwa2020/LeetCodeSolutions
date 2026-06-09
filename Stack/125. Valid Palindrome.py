class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        # s = s.replace(" ", "").replace(",", "").replace(":", "").replace(".","").replace("/","").replace("@","").replace("#","").replace("_","")
        import re
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)
        s_rev = "".join(reversed(s))
        if s == s_rev:
            return True
        else:
            return False

        # for i in range(len(s)):
        #     if s[i] != s[-i-1]:
        #         return False
            
        # return True