class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            # Try to put the lightest and heaviest person together
            if people[left] + people[right] <= limit:
                left += 1

            # Heaviest person always needs a boat
            right -= 1
            boats += 1

        return boats