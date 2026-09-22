class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = (total // k)
        nums.sort(reverse = True)

        if nums[0] > target:
            return False

        bucket = [0] * k

        def backtrack(index):
            if index == len(nums):
                return True

            num = nums[index]

            for i in range(k):
                if bucket[i] + num > target:
                    continue

                bucket[i] += num

                if backtrack(index + 1):
                    return True

                bucket[i] -= num

                if bucket[i] == 0:
                    break

            return False

        return backtrack(0)