def canAttendMeetings(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        prev = intervals[i-1]
        if intervals[i][0] < prev[1]:
            return False
    return True
