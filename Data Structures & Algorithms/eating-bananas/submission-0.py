class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            hours = 0

            # Calculate total hours needed at speed = mid
            for bananas in piles:
                hours += (bananas + mid - 1) // mid   # ceil(bananas / mid)

            if hours <= h:
                # This speed works, try a smaller one
                high = mid - 1
            else:
                # Too slow, increase the speed
                low = mid + 1

        return low