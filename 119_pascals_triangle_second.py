from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row  = [1] * (numRows+1)

        for i in range(2, numRows+1):
            for j in range(i-1,0,-1):
                row[j] = row[j-1] + row[j]

        return row
sol = Solution()
print(sol.generate(3))
