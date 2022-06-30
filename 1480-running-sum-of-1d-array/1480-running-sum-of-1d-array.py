class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        sol = []
        for i in nums:
            sol.append(sum+i)
            sum = sum +i
        return sol