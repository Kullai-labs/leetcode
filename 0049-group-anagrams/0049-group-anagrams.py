class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # str=sorted(str)
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))   # signature: sorted letters
            if key not in groups:
                groups[key] = []           # create bucket if it doesn't exist
            groups[key].append(word)       # add word to its bucket
        return list(groups.values())
