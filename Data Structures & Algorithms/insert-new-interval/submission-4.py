class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # to find overlapping intervals:
        # we need to find the lowest start and highest end among these overlapping intervals

        if (len(intervals) == 0):
            return [newInterval]

        start = newInterval[0]
        end = newInterval[1]
        i = 0
        while i < len(intervals):
            if (start <= intervals[i][0] and end >= intervals[i][1]) or (start >= intervals[i][0]
            and start <= intervals[i][1]) or (start <= intervals[i][0] and end >= intervals[i][0]):
                # setting the end overlapping limits
                if start > intervals[i][0]:
                    start = intervals[i][0]
                if end < intervals[i][1]:
                    end = intervals[i][1]
                
                intervals.pop(i) # remove the overlapped interval

            elif intervals[i][0] > start: # no more overlaps + correct insertion point
                intervals.insert(i, [start, end])
                break
            else:
                i += 1

        if (len(intervals) == 0): # because if there is no more intervals, we have to add in manually
            return [[start, end]]
        elif intervals[len(intervals)-1][0] < start: 
            intervals.append([start, end])

        return intervals
