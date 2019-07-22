'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, i: int, j: int) -> int:
        s=sum(self.nums[i:(j+1)])
        return s
