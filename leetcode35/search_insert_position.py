"""

35. 搜索插入位置
简单
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。


示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4
 

提示:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为 无重复元素 的 升序 排列数组
-104 <= target <= 104

"""

from typing import List

class Solution:
    # 解法1 按序查找
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)

    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)
    
    # 解法2 二分查找
    # 时间复杂度：O(logn)
    # 空间复杂度：O(1)
    # 思路：二分查找，找到目标值则返回索引，否则返回左指针
    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
        
if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,5,6]
    target = 5
    assert solution.searchInsert(nums, target) == 2
    assert solution.binary_search(nums, target) == 2

    nums = [1,3,5,6]
    target = 2
    assert solution.searchInsert(nums, target) == 1
    assert solution.binary_search(nums, target) == 1

    nums = [1,3,5,6]
    target = 7
    assert solution.searchInsert(nums, target) == 4
    assert solution.binary_search(nums, target) == 4