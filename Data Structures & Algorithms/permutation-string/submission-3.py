class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        for i in range(len(s1)):
            if s1[i] in map1:
                map1[s1[i]] += 1
            else:
                map1[s1[i]] = 1

        map2 = {}
        left = 0
        for right in range(len(s2)):

            if s2[right] in map2:
                map2[s2[right]] += 1
            else:
                map2[s2[right]] = 1
            
            while (right - left + 1) > len(s1):
                map2[s2[left]] -= 1
                if map2[s2[left]] == 0:
                    del map2[s2[left]]
                left += 1
            
            if map1 == map2:
                return True
        return False