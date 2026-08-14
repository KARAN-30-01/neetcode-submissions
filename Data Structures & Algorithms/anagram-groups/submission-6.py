class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def check(str1):
            freq = {}
            for i in str1:
                freq[i] = freq.get(i, 0) + 1
            return tuple(sorted(freq.items()))

        groups = {}

        for i in strs:
            key = check(i)

            if key not in groups:
                groups[key] = []

            groups[key].append(i)

        return list(groups.values())