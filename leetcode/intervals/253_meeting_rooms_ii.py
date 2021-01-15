def minMeetingRooms(intervals):
    start = [0]*len(intervals)
    end = [0]*len(intervals)

    for i in range(len(intervals)):
        start[i] = intervals[i][0]
        end[i] = intervals[i][1]
    start.sort()
    end.sort()
    startPter, endPter, meetingRooms = 0, 0, 0

    while startPter < len(intervals):
        if start[startPter] < end[endPter]:
            meetingRooms += 1
        else:
            endPter += 1

        startPter += 1
    return meetingRooms
