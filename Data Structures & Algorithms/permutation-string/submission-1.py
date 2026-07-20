from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        if k > n:
            return False
        s1_count = Counter(s1)
        l = 0
        r = k - 1
        checker = {}
        for i in range(k):
            checker[s2[i]] = 1 + checker.get(s2[i],0)
        while r < n - 1:
            if checker == s1_count:
                return True
            else:
                checker[s2[l]] -= 1
                if checker[s2[l]] == 0:
                    del checker[s2[l]]
                l += 1
                r += 1
                checker[s2[r]] = 1 + checker.get(s2[r],0)
        return checker == s1_count

        


        
        