def maxProfit(self, prices: List[int]) -> int:
     max_profit = 0
      lowest = float("inf")
       for i in range(0, len(prices)):
            lowest = min(lowest, prices[i])
            max_profit = max(max_profit, prices[i] - lowest)

        return max_profit
