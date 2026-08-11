class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {ch: i for i, ch in enumerate(s)}
        used = set()
        ans = []

        for i, ch in enumerate(s):
            if ch in used:
                continue

            while ans and ans[-1] > ch and last[ans[-1]] > i:
                tem = ans.pop()
                used.remove(tem)

            ans.append(ch)
            used.add(ch)

        return "".join(ans)