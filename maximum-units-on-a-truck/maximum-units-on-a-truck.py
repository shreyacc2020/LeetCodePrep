class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        
        capacity = 0
        
        for box,unit in boxTypes:
            if truckSize >= box:
                truckSize -= box
                capacity += unit*box
            else:
                capacity += truckSize*unit
                break
        return capacity