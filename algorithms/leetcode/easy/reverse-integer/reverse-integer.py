class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # splicing in python
        # list[<start>:<stop>:<step>]
        # [::-1] starts from the end of the string and reverses it
        answ = (1, -1)[x < 0] * int(str(abs(x))[::-1])
        if (answ >= - 2 ** 31 and answ <=  2 ** 31 - 1):
            return(answ)
        else:
            return(0)


# if x = 123 return 321
# if x = -1 return 1
# if x = 120 return 21

solution = Solution()
x = 210
print(solution.reverse(x))
