class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # soritng the intervals
        merged = [intervals[0]] # starting with the first element

        for interval in intervals:
            if merged[-1][1] < interval[0]: # complaring with the last element of merged[]
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


        