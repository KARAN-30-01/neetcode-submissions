class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups: dict[str, List[str]] = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in anagram_groups:
                anagram_groups[sorted_string].append(string)
            else:
                anagram_groups[sorted_string] = [string]
        ans = []
        for group in anagram_groups.values():
            ans.append(group)
        return ans