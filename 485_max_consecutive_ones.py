"""

"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_run = 0
        for n in nums:
            if n == 1:
                current_run += 1
                if current_run > max_consecutive: max_consecutive = current_run
            else:
                current_run = 0
        
        return max_consecutive
                

sol = Solution()