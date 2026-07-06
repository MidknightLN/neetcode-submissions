class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))


        individuals = []

        reached_start = -1
        reached_end = -1

        for start, end in  intervals:
            if start > reached_end:
                individuals.append([reached_start, reached_end])
                reached_start = start
                reached_end = end
            else:
                reached_end = max(reached_end, end)

        individuals.append([reached_start, reached_end])
        return individuals[1:]