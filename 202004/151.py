import re
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(re.split(' +',s))

if __name__ == "__main__":
    s = "a good   example"

    res = Solution()
    print(res.reverseWords(s))