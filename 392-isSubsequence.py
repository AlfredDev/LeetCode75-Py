#392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false
#  otherwise.

# Example 1:
################################
# Input: s = "abc", t = "ahbgdc"
# Output: true

class Solution():
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) > len(t)): return False
        sub = 0
        for i in range(len(t)):
            if(sub <= len(s) - 1):
              if (s[sub] == t[i]):
                sub += 1
        return sub == len(s)

    def isSubsequence2(self, s, t):
        i = 0 
        j = 0

        while i < len(s) and j < len(t):
            if (s[i] == t[j]):
             i += 1
            j += 1     
        return i == len(s)
        

s = Solution()

#print(s.isSubsequence('abc','ahbgdc'))
print(s.isSubsequence2('abc','ahbgdc'))