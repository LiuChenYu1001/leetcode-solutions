from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def at_least(k):
            vowel = "aeiou"
            n = len(word)
            consonants = 0
            left = 0
            ans = 0
            count = Counter()

            for right in range(n):
                ch = word[right]

                if ch in vowel:
                    count[ch] += 1
                else:
                    consonants += 1

                while len(count) == 5 and consonants >= k:
                    ch = word[left]

                    ans += n - right

                    if ch in vowel:
                        count[ch] -= 1

                        if count[ch] == 0:
                            del count[ch]

                    else:
                        consonants -= 1

                    left += 1

            return ans

        return at_least(k) - at_least(k + 1)