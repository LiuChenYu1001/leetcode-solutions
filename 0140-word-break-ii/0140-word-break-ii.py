class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        n = len(s)
        dp = {}

        def dfs(start):
            if start in dp:
                return dp[start]

            if start == n:
                return [""]

            sentence = []

            for end in range(start + 1, n + 1):
                word = s[start:end]

                if word not in word_set:
                    continue

                for suffix in dfs(end):
                    if suffix:
                        sentence.append(word + " " + suffix)
                    else:
                        sentence.append(word)

            dp[start] = sentence
            return sentence

        return dfs(0)