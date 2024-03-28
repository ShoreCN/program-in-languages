
"""
121. 买卖股票的最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

# 解法一：暴力解法
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
# 思路：遍历每一天，然后再遍历后面的每一天，计算利润，取最大值
# 问题：超时, 时间复杂度太高

class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for num, price in enumerate(prices):
            for sell_price in prices[num+1:]:
                if sell_price > price:
                    max_profit = max(max_profit, sell_price - price)

        return max_profit
    

class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 解法二
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 思路：遍历每一天，记录最低价格，然后计算利润，取最大值
        
        lowest_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < lowest_price:
                lowest_price = price
            else:
                max_profit = max(max_profit, price - lowest_price)

        return max_profit


if __name__ == '__main__':
    solution = Solution1()
    solution2 = Solution2()

    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))
    assert solution.maxProfit(prices) == 5
    assert solution2.maxProfit(prices) == 5

    prices = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices))
    assert solution.maxProfit(prices) == 0
    assert solution2.maxProfit(prices) == 0
