class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers i, j where i => buy day and j => sell day
        # iterate i: 0 -> n - 2
        # iterate j: 1 -> n - 1
        # if buy >= sell => better buy at this date => move buy to current sell
        # if buy < sell => we can sell at this date, record current profit, but try to sell in the next date to see if we can get a better profit.
        # if next date returns better profit, then record the new profit
        n = len(prices)
        if n == 1:
            return 0
        max_profit = 0
        buy = sell = 0
        while sell < n:
            if prices[buy] <= prices[sell]:
                # Check max profit
                max_profit = max(max_profit, prices[sell] - prices[buy])
                # Try to sell in the next date
                sell += 1
            else:
                # prices[buy] > prices[sell]. Should buy at this sell date
                buy = sell
        return max_profit


        