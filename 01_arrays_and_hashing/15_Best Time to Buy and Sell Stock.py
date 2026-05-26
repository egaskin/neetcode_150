from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices = [p_0, p_1, ... p_n]
        prices[i] = p_i
        best_diff[i] = p_i - min(prices[0:i])

        min(prices[0:i]) is the minimum price seen so far if we are
        iterating over the the prices array. we can save this value
        and update it as we go to calculate the best_diff[i] which
        is the best profit that can be achieved on day i
        given the prices from the 0th day to the ith day
        """
        if len(prices) < 2:
            return 0

        min_price_so_far = prices[0]
        cur_diff = prices[1] - prices[0]
        max_diff = cur_diff
        for i in range(1, len(prices)):
            # consider current price versus the min so far
            cur_diff = prices[i] - min_price_so_far
            if max_diff < cur_diff:
                max_diff = cur_diff

            if min_price_so_far > prices[i]:
                min_price_so_far = prices[i]

        if max_diff < 0:
            return 0
        return max_diff

class Solution_BruteForce:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = -float("inf")
        for i in range(0, len(prices)):
            for j in range(i, len(prices)):
                # on day j, sell the stock bought previously on day i
                cur_diff = prices[j] - prices[i]
                if cur_diff > max_diff:
                    max_diff = cur_diff
                print(f"i = {i}, j = {j}, cur_diff = {cur_diff}, max_diff = {max_diff}")

        if max_diff > -float("inf"):
            return max_diff # type: ignore
        
        return 0
    
if __name__ == "__main__":
    prices=[7,1,5,3,6,4]
    Solution_BruteForce().maxProfit(prices)