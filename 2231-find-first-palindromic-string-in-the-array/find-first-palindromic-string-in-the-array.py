class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res=""
        for i in words:
            a=i[::-1]
            if res == "":
                if i == a:
                    res=i
        return res
        