class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximum_profit = 0
        # brute force
        # for initial_price_idx in range(len(prices)):
        #     initial_price = prices[initial_price_idx]
        #     for current_price_idx in range(initial_price_idx + 1, len(prices)):
        #         current_price = prices[current_price_idx]
        #         current_profit = current_price - initial_price
        #         maximum_profit = max(maximum_profit, current_profit)

        ####### approch 2 start
        # let's dry run
        # [7, 1, 5, 3, 6, 4]
        # iter 0, idx = 1:
        # current_price = 1
        # prev_min_price = 7
        # maximum_profit = max(0, -6) =>  0
        # Cond: True => prev_min_price_idx = 1
        # iter 1, idx = 2:
        # current_price = 5
        # prev_min_price = 1
        # maximum_profit = max(0, 4) =>  4
        # Cond: False => prev_min_price_idx = 1
        # iter 2, idx = 3:
        # current_price = 3
        # prev_min_price = 1
        # maximum_profit = max(4, 2) =>  4
        # Cond: False => prev_min_price_idx = 1
        # iter 3, idx = 4:
        # current_price = 6
        # prev_min_price = 1
        # maximum_profit = max(4, 5) =>  5
        # Cond: False => prev_min_price_idx = 1
        # iter 4, idx = 5:
        # current_price = 4
        # prev_min_price = 1
        # maximum_profit = max(5, 3) =>  5
        # Cond: False => prev_min_price_idx = 1
        # maximum_profit = 0
        # prev_min_price_idx  = 0
        # for idx in range(1, len(prices)):
        #     current_price = prices[idx]
        #     prev_min_price = prices[prev_min_price_idx]
        #     maximum_profit = max(maximum_profit, current_price - prev_min_price)
        #     if current_price <  prev_min_price:
        #         prev_min_price_idx = idx
        # return maximum_profit
        ####### approch 2 ends

        # kadan's alogirthm
        max_current = 0
        max_so_far = 0
        for idx in range(1, len(prices)):
            max_current += prices[idx] - prices[idx - 1]
            max_current = max(0, max_current)
            max_so_far = max(max_current, max_so_far)
        return max_so_far
