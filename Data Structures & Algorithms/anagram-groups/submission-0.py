class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checker = {}
        for char in strs:
            word = "".join(sorted(char))
            if word in checker:
                checker[word].append(char)
            else:
                checker[word] = [char]
        return list(checker.values())