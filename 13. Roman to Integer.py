class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst=list(s)
        lst.append(0)
        sum = 0
        for i in range(len(lst)-1):
            if lst[i] == 'I':
                if ((lst[i+1]) == 'V' or (lst[i+1] == 'X')):
                    sum -= 1
                else:
                    sum += 1
            elif lst[i] == 'V':
                sum += 5
            elif lst[i] == 'X':
                if lst[i+1] == 'L' or lst[i+1] == 'C':
                    sum -= 10
                else:
                    sum += 10
            elif lst[i] == 'L':
                sum += 50
            elif lst[i] == 'C':
                if lst[i+1] == 'D' or lst[i+1] == 'M':
                    sum -= 100
                else:
                    sum += 100
            elif lst[i] == 'D':
                sum += 500
            elif lst[i] == 'M':
                sum += 1000
        return sum