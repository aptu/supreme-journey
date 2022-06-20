# 121. Best Time to Buy and Sell Stock
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    maxprofit = 0
    left, right = 0, 1
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxprofit = max(maxprofit, profit)
        else:
            left = right
        right += 1
    return maxprofit


def main():
    print(maxProfit([7,1,5,3,6,4]))  # == 5

main()

def test():
    assert (maxProfit([7,1,5,3,6,4]) == 5)