class Solution:

    #  O(N^2)
    # def maxProfit(self, prices: List[int]) -> int:
    #     max_profit = 0
    #     first_day = 0
    #     for index in range(len(prices)):
    #         first_day = index
    #         second_day = first_day + 1
    #         for jindex in range(second_day, len(prices)):
    #             profit = prices[jindex] - prices[index]
    #             # print(profit)
    #             if  profit > max_profit:
    #                 max_profit = profit
        
    #     return max_profit

    # O(N)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')  # Start with a very large minimum price

        for price in prices:
            # print("before => "+ str(min_price) + ", " + str(price))
            min_price = min(min_price, price)  # Keep track of the minimum price encountered
            # print("after "+ str(min_price))
            profit = price - min_price  # Calculate potential profit for the current day
            max_profit = max(max_profit, profit)  # Update max_profit if necessary

        return max_profit

            
        