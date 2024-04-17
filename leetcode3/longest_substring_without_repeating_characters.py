
"""
3. 无重复字符的最长子串
中等
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。


示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        max_r = 0
        sub_str = ""
        for c in s:
            if c in sub_str:
                sub_str = sub_str[sub_str.index(c)+1:] + c
                max_r = max(max_r, r)
                r = len(sub_str)
            else:
                sub_str += c
                r += 1
        
        max_r = max(max_r, r)
        return max_r
    

if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    assert solution.lengthOfLongestSubstring(s) == 3

    s = "bbbbb"
    assert solution.lengthOfLongestSubstring(s) == 1

    s = "pwwkew"
    assert solution.lengthOfLongestSubstring(s) == 3

    s = ""
    assert solution.lengthOfLongestSubstring(s) == 0

    s = "dvdf"
    assert solution.lengthOfLongestSubstring(s) == 3