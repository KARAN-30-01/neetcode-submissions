class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_ang = {}
        for item in strs:
            temp = "".join(sorted(item))
            if temp not in group_ang:
                group_ang[temp] = [item]
            else:
                group_ang[temp].append(item)
        
        return list(group_ang.values())

        