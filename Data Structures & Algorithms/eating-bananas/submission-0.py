class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            hours = 0

            # calculate total hours needed at speed = mid
            for p in piles:
                hours += (p + mid - 1) // mid   # ceiling division

            if hours > h:
                l = mid + 1   # too slow, increase speed
            else:
                r = mid       # fast enough, try smaller speed

        return l
