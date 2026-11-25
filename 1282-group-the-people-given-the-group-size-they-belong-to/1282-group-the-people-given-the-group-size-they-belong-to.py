class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        group = {}
        ans = []

        for i, size in enumerate(groupSizes):
            if size not in group:
                group[size] = []

            group[size].append(i)

            if len(group[size]) == size:
                ans.append(group[size])
                group[size] = []

        return ans