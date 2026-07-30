class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=sorted(nums1+nums2)
        l=len(n)
        if l%2==1:
            return n[l//2]
        else:
            return (n[l//2-1]+n[l//2])/2