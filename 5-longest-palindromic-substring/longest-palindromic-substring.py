class Solution:
    def longestPalindrome(self, s: str) -> str:
        # longest=""
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         substring=s[i:j+1]

        #         if substring == substring[::-1]:
        #             if len(substring) > len(longest):
        #                 longest=substring
        # return longest

        if len(s) == 0:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            # Odd length palindrome
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (end - start):
                    start = l
                    end = r
                l -= 1
                r += 1

            # Even length palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (end - start):
                    start = l
                    end = r
                l -= 1
                r += 1

        return s[start:end+1]

        