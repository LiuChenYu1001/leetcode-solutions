class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_place = {}
        for i, ch in enumerate(s):
            last_place[ch] = i
        
        result = []
        end, start = 0, 0

        for i, ch in enumerate(s):
            end = max(end, last_place[ch])
            if i == end:
                result.append(end-start+1)
                start = i + 1

        return result