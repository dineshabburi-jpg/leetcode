class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        prefix = 0
        seen = {0: -1}
        answer = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            # We need:
            # (prefix - previous_prefix) % p == target
            needed = (prefix - target) % p

            if needed in seen:
                answer = min(answer, i - seen[needed])

            seen[prefix] = i

        # Cannot remove the entire array
        if answer == len(nums):
            return -1

        return answer