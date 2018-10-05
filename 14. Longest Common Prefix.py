class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # A dedicate version using unzip and enumerate.
        for index, letter_sep in enumerate(zip(*(strs))):
            if len(set(letter_sep)) > 1:
                return strs[0][:index]
        else:
            return min(strs)