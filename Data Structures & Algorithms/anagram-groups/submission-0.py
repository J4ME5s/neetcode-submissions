class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in map:
                map[key] = []
            map[key].append(word)
        return list(map.values())