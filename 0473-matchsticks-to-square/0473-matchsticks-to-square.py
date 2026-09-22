class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum( matchsticks)
        
        if total % 4 != 0:
            return False

        target = total // 4
        matchsticks.sort(reverse = True)

        if matchsticks[0] > target:
            return False

        sides = [0] * 4
        def backtrack(idx):
            if idx == len( matchsticks):
                return True

            for j in range(4):
                if sides[j] +  matchsticks[idx] <= target:
                    sides[j] +=  matchsticks[idx]

                    if backtrack(idx + 1):
                        return True

                    sides[j] -=  matchsticks[idx]

            return False

        return backtrack(0)