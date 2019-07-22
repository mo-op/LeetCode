'''Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.'''


import collections 

class Solution(object):
    def countFrequency(self, arr): 
        return collections.Counter(arr) 
    
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = self.countFrequency(arr1)
        arr3 = []
        temp = []
        
        if len(arr1) == 0:
            return []
        if len(arr2) == 0:
            return arr1
        # elements in arr2 
        for x in arr2:
            if x in count.keys():
                cur_el = [x for y in range(0,count[x])] 
                arr3 += cur_el
        
        for x in arr1:
            if x not in arr3:
                temp.append(x)
        
        return(arr3 + sorted(temp))
        
