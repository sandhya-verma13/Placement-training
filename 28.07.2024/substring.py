from itertools import permutations

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        perm_list = list(permutations(words))
        concat_strings = [''.join(perm) for perm in perm_list]
        indexs = []
        for word in concat_strings:
            start = 0
            while True:
                index_val = s.find(word, start)
                if index_val == -1:
                    break
                indexs.append(index_val)
                start = index_val + 1
        return list(set(indexs)
