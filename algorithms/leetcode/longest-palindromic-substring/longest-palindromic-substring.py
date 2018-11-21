class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        start = 0
        end = 0
        longest = 0
        for i in range(0, len(s)):


            # for palindromes like 'aba'
            length1= 1
            left = i
            right = i
            start1 = 0
            end1 = 0
            while (right <= len(s)-1) & (left >= 0):
                if s[left] == s[right]:
                    start1 = left
                    end1 = right
                    left -= 1
                    right += 1
                else:
                    break
            length1= end1 - start1
            if length1 > longest:
                start = start1
                end = end1
                longest = length1

            # for palindromes like 'abba'
            length2 = 1
            left = i
            right = i+1
            start2 = 0
            end2 = 0
            while (right <= len(s)-1) & (left >= 0):
                if s[left] == s[right]:
                    start2 = left
                    end2 = right
                    left -= 1
                    right += 1
                else:
                    break
            length2 = end2 - start2
            if length2 > longest:
                start = start2
                end = end2
                longest = length2

        return s[start:end+1]

solution = Solution()
s = "abbaaa"
print(solution.longestPalindrome(s))
