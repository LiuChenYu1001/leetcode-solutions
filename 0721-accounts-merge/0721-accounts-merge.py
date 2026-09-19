from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        parents = list(range(n))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])

            return parents[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                parents[px] = py

        emails_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emails_to_account:
                    union(i, emails_to_account[email])
                else:
                    emails_to_account[email] = i

        groups = defaultdict(list)
        for email, account_idx in emails_to_account.items():
            root = find(account_idx)
            groups[root].append(email)

        ans = []
        for root, emails in groups.items():
            ans.append([accounts[root][0]] + sorted(emails))

        return ans