# Best Time to Buy and Sell Stock II

# Say you have an array prices for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Input: [7,1,5,3,6,4]
# Output: 7

# Input: [1,2,3,4,5]
# Output: 4

# Input: [7,6,4,3,1]
# Output: 0

def maxProfit(prices):
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i]>prices[i-1]:
            maxProfit += prices[i]-prices[i-1]
    return maxProfit
