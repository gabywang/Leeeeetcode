class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # count() method returns the number of occurrences of the substring in the given string.
        return sum(map(J.count, S))