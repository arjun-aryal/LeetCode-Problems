"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
 


"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        ans = ""
        sort = sorted(strs)
        for i in range(min(len(sort[0]),len(sort[-1]))):
            if sort[0][i] != sort[-1][i]:
                return ans
            ans += sort[0][i]
        return ans



obj = Solution()
a =obj.longestCommonPrefix(strs = ["flower","flow","flight"])
b=  obj.longestCommonPrefix(strs = ["dog","racecar","car"])

print(f'["flower","flow","flight"] :     {a}')

print(f'["dog","racecar","car"]:    {b}')
