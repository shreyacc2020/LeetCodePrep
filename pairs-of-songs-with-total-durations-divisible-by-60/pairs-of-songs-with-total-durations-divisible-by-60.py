# Shreya Chnadwadkar
# Strategy 1 :
# -------------Gave TLE-------------
# 1. Keep two pointers, i and i+1
# 2. Check if sum is divisible by 60
# 3. If yes, increase count by 1
# 4. Return count
# -------------Gave TLE-------------(as expected) 
# Strategy 2 :
# 1. Sort the list first
# 2. Keep two pointers, i and i+1
# 3. Check if sum is divisible by 60
# 4. If yes, increase count by 1
# 5. Return count
# --------------------------
# Strategy 3 :
# No need for sorting
# 1. Create a hash map of count of remainders of the elements.
# 2. Then for each element, check if the subtracted element exists in hashmap
# 3. If it does, increase the pairs count and increase the count of the remainder in hashmap
# 4. If it dosen't, move to the next element.
# 5. Return count

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        hashmap = {}
        for i in time:
            remainder = i%60
            
            if remainder == 0:
                if remainder in hashmap:
                    count+=hashmap[remainder]
            elif (60-remainder) in hashmap:
                count += hashmap[60-remainder]
            if remainder in hashmap:
                hashmap[remainder] +=1
            else:
                hashmap[remainder] = 1
        return count
        
        
        return count