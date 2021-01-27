class UndergroundSystem:

    def __init__(self):
        self.train = {}
        self.avgTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.train[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (startStation, startTime) = self.train[id]
        if (f'{startStation}to{stationName}' in self.avgTimes):
            (count, avgTime) = self.avgTimes[f'{startStation}to{stationName}']
            count += 1
            avgTime = (avgTime*(count-1) + (t-startTime))/count
            self.avgTimes[f'{startStation}to{stationName}'] = (count, avgTime)
        else:
            self.avgTimes[f'{startStation}to{stationName}'] = (1, t-startTime)
        del self.train[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        (count, avgTime) = self.avgTimes[f'{startStation}to{endStation}']
        return avgTime
