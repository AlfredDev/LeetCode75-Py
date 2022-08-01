class Solution:
    def longestPalindrome(self, s: str) -> int:

        char_dict = {}

        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        
        if len(char_dict) == 1:
            return char_dict[s[0]]
        
        res = 0
        odd = 0

        for i in char_dict.values():
            if i > 1:
                if i %2 == 0:
                    res = res + 1
                else:
                    res += i -1
                    odd += 1
            else:
             odd += 1
        if odd > 0:
            res += 1
        
        return res

    


