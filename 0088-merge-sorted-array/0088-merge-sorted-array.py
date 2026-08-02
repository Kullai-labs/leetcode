class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        slow=0
        for fast in range(m,len(nums1)):
            nums1[fast]=nums2[slow]
            slow+=1
        nums1.sort()

        