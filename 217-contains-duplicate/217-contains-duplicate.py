class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        return((len(temp)!=len(nums)))
        