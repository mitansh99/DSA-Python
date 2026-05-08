class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 1
        hash1 = {}
        
        for idx in range(len(position)):
            hash1[position[idx]] = speed[idx]
            
        position.sort(reverse=True)
        fleet_time = (target-position[0])/hash1[position[0]]
        
        for idx in range(1, len(position)):
            time = (target-position[idx])/hash1[position[idx]]
            if time > fleet_time:
                fleet_count += 1
                fleet_time = time

        return fleet_count