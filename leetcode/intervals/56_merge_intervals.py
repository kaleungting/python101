def merge(intervals):
    intervals.sort()
    result = [intervals[0]]
    for interval in intervals:
        last = result[-1]
        if interval[0] <= last[1]:
            result[-1][1] = max(interval[1], last[1])
        else:
            result.append(interval)
    return result
