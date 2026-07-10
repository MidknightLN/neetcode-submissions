"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        from collections import defaultdict

        time_diff = defaultdict(int)
        # 記錄每個時間點的淨變化量
        for node in intervals:
            time_diff[node.start] += 1
            time_diff[node.end] -= 1
            
        current_rooms = 0
        max_rooms = 0
        
        # 精髓在於這行：必須按照「時間順序」從早到晚處理
        for time in sorted(time_diff.keys()):
            current_rooms += time_diff[time]
            max_rooms = max(max_rooms, current_rooms)
            
        return max_rooms