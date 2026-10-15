class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        if 1 in nums:
            return False

        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return

            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x

            parent[root_y] = root_x
            size[root_x] += size[root_y]

        prime_to_idx = {}

        for i, num in enumerate(nums):
            factor = 2

            while factor * factor <= num:
                if num % factor == 0:

                    if factor in prime_to_idx:
                        union(i, prime_to_idx[factor])
                    else:
                        prime_to_idx[factor] = i

                while num % factor == 0:
                    num //= factor

                factor += 1

            if num > 1:
                if num in prime_to_idx:
                    union(i, prime_to_idx[num])
                else:
                    prime_to_idx[num] = i

        root = find(0)

        return all(find(i) == root for i in range(n))