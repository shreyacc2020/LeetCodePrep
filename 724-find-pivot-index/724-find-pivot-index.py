class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            left_sum, right_sum = 0,0
            right_sum = sum(nums[i+1:len(nums)])
            left_sum = sum(nums[0:i])
            if (left_sum == right_sum):
                return i
        return -1