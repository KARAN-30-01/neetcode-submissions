class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_hash_list = {}
        for _ in strs:
            key = tuple(sorted(_))
            if(key in freq_hash_list):
                freq_hash_list[key].append(_)
            else:
                freq_hash_list[key] = [_]
            

        return list(freq_hash_list.values())