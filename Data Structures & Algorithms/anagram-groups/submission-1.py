class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        resmap = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in resmap:
                resmap[sortedword].append(word)
            else:
                resmap[sortedword] = [word]
        for listwords in resmap.values():
            result.append(listwords)
        return result
                
            