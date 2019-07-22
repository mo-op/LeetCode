'''
Given an integer, write a function to determine if it is a power of three.
'''
## with loop

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        x = n 
        while(x > 3):
            x /= 3
        if x == 3:
            return True
        return False
'''
## without loop
## note: not my brainchild, this is just for my reference & yours if you've taken a detour to this file
class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0
'''
