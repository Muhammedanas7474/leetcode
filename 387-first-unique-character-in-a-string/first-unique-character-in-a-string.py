class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count=Counter(s)

        # for i,v in enumerate(s):
        #     if count[v] == 1:
        #         return i
        # return -1

        freq={}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i]=1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
            