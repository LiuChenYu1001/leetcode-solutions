from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        for frm, to in tickets:
            graph[frm].append(to)

        for frm in graph:
            graph[frm].sort(reverse = True)

        ans = []

        def dfs(frm):
            while graph[frm]:
                nxt_airport = graph[frm].pop()
                dfs(nxt_airport)
            
            ans.append(frm)

        dfs("JFK")

        return ans[::-1]