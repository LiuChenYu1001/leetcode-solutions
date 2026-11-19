class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        job = sorted(zip(difficulty, profit))
        worker.sort()

        ans = max_profit = i = 0

        for ability in worker:
            while i < len(job) and job[i][0] <= ability:
                max_profit = max(max_profit, job[i][1])
                i += 1

            ans += max_profit

        return ans