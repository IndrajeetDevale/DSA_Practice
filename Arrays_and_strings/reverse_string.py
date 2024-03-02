class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            a = s[left]
            b = s[right]
            
            s[left] = b
            s[right] = a
            
            left += 1
            right -= 1
            
