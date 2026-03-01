class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long=0
        for i in range(len(s)):
            seen=""
            for j in range(i,len(s)):
                char=s[j]
                if char not in seen:
                    seen=seen+char
                else:
                    break
            if len(seen)>long:
                long=len(seen)
        return long
