def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    totalCost = 0

    costs.sort(key=lambda x: x[0] - x[1])

    #find the half
    n = len(costs)//2
    for i in range(n):
        totalCost += costs[i][0] + costs[i+n][1]
        #send first half to A, second half to B
    return totalCost
