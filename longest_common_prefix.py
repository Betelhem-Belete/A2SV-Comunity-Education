class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        if not strs:
            return ""
        # length of the minimum string in the list
        min_length = min(len(s) for s in strs)

        # iterate characters upto the minimum length
        for i in range(min_length):
            char_first = strs[0][i]

            if all(s[i] == char_first for s in strs):
                pre += char_first
            else:
                break
        return pre
