class Solution:
    def firstPalindrome(self, words) -> str:
        def check(s):
            if s==s[::-1]:
                return True
            else:
                return False
        for i in words:
            if check(i):
                return i
        return ""