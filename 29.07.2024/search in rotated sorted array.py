class Solution:
    def search(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(0,len(nums)):
            if nums[i]==target:
                return c
            else:
                c+=1
        return -1
