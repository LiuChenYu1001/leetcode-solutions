class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

        ans = []

        for word in words:
            w = word.lower()

            for row in rows:
                if w[0] in row:
                    if all(ch in row for ch in w):
                        ans.append(word)
                    break

        return ans