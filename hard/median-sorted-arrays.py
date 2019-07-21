class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)> 0 or len(nums2) > 0:
            merged = sorted(nums1 + nums2)
            if len(merged) % 2 == 0:
                md_ind2 = int(len(merged)/2)
                md_ind1 = md_ind2-1
                return(float(int(merged[md_ind1]+merged[md_ind2])/2))
            else:
                md_ind1 = int((len(merged)-1)/2)
                return(float(merged[md_ind1]))
        else:
            return 0.0
