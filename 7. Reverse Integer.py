class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0

        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)

        while x != 0:
            rev = 10*rev + x%10
            x = x//10
        if (rev>pow(2,31)-1):
            return 0
        return rev*sign