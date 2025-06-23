from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        distance = 0
        water_can = capacity
        x = 0
        for i, water_plant in enumerate(plants):
            if water_can < water_plant:
                water_can = capacity
                distance += i * 2
            water_can -= water_plant
            distance += 1
        return distance

print(Solution().wateringPlants([2,2,3,3], 5)) # 14
print(Solution().wateringPlants([1,1,1,4,2,3], 4)) # 30
print(Solution().wateringPlants([7,7,7,7,7,7,7], 8)) # 49