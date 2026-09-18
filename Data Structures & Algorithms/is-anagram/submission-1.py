class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for j in countS:
        #     if countS[j] != countT.get(j, 0):
        #         return False

        # return True   
        lenS = len(s)
        lenT = len(t)

        if lenS != lenT:
            return False

        freqS = {}
        freqT = {}

        for char in s:
            freqS[char] = freqS.get(char, 0) + 1
        
        for char in t:
            freqT[char] = freqT.get(char, 0) + 1
        
        if freqS == freqT:
            return True
        
        return False
        