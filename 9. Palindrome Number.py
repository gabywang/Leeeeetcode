class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 10 and x >= 0):
            return True
        elif x < 0:
            return False
        else:
            dic = {}
            count = 0
            i = 0
            while x!= 0:
                dic[i] = x%10
                x = x//10
                count += 1
                i += 1
            for i in range(count//2+1):
                if dic[i] != dic[count-i-1]:
                    return False
            return True