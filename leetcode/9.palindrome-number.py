#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            x = x*(-1)
        birbas = x % 10
        onbas = int(((x % 100) - birbas)/10)
        yüzbas = int(((x % 1000) - (x % 100))/100)
        binbas = int(((x % 10000)-(x % 1000))/1000)
        onbinbas = int(((x % 100000)-(x % 10000))/10000)
        yüzbinbas = int(((x % 1000000)-(x % 100000))/100000)
        if x > 10:
            if x/10 > 0 and x % 10 < 10:
                if birbas == onbas:
                    return True
            if x/100 > 0 and x % 100 < 10:
                if birbas == yüzbas:
                    return True
            if x/1000 < 0 and x % 1000 < 10:
                if birbas == binbas and yüzbas == onbas:
                    return True
        else:
            return False


# @lc code=end

print(Solution.isPalindrome(1, -1111))
