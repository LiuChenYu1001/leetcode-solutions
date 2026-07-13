class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr = sorted(set(arr))

        idx = {}
        for i, num in enumerate(new_arr):
            idx[num] = i

        ans = []
        for num in arr:
            ans.append(idx[num] + 1)

        return ans