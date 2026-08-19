from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        ans = []

        for num, count in freq.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans