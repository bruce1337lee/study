class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype int
        """

        # solution for strings like '405' or '    405' or ' -405'...

        # go through str chars
        # if space ignroe
        # if num -> retval += num * 1 * 10 ** time after space

        length = len(str)
        negFlag = False
        retVal = 0

        for i in str:
            if i != ' ':
                if i != '-':
                    iVal = ord(i) - 48
                    retVal += iVal * (10 ** (length-1))
                else:
                    negFlag = True

            length -= 1

        return (1, -1)[negFlag != False] * retVal

solution = Solution()
myInt = "405"
print(solution.myAtoi(myInt))
