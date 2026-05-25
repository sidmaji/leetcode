---
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
difficulty: Easy
topics:
  - array
  - dynamic-programming
---
# Best Time to Buy and Sell Stock

## Approach
First, initialize `buy`, which will keep track of the smallest price in `prices`. Then `profit` is set to 0.

Iterating through `prices`, `buy` is updated if the current price is lower, and `profit` is updated if the current price minus the smallest buy price found thus far is lower than `profit`. This ensures that the highest profit is found dynamically, as the highest profit might not come from buying the smallest buy price (eg. `prices = [2, 5, 1, 3]`, where the highest profit would be `prices[1] - prices[0]`. So in the loop, `buy` will update as the price of `1` is lower than `2`, but `profit` won't update past index 1.

## Solution
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
```

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)