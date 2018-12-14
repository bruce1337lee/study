class Solution(object):
    def isMatch(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))

        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


solution = Solution()
s = "something"
p = "something"
solution.isMatch(s, p)