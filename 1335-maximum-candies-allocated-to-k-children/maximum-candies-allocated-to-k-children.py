class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        left = 1
        right = max(candies)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            # Count how many piles of size 'mid' we can make
            total = 0
            for candy in candies:
                total += candy // mid

                if total >= k:
                    break

            if total >= k:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer