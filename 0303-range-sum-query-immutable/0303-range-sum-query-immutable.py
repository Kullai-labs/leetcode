class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
    # ans=[]


    def sumRange(self, left: int, right: int) -> int:
        # ans=[]
        # ans.append(sum(nums[left:right+1]))
        # return ans
        sum1=0
        for i in range(left,right+1):
           sum1+=self.nums[i]
        return sum1
          

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)