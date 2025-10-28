from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []

        keys = [set("qwertyuiop"),set("asdfghjkl"), set("zxcvbnm")]

        for word in words:
            lword = set(word.lower())
            if any(lword <= key for key in keys):
                ans.append(word)

        return ans
                

sol = Solution()
print(sol.findWords(["Hello","Alaska","Dad","Peace"]))