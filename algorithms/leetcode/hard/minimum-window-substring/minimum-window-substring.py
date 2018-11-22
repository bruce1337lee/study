class Solution(object):
    def minWindowSubstring(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        count = 0
        shortest = len(s)
        start = 0
        end = 0
        mstart = 0
        mend = 0
        for i in range(0, len(s)):
            expandRet = self.expandFromCenter(s, t, i)
            print(expandRet)
            count = expandRet[0]
            mstart = expandRet[1]
            mend = expandRet[2]
            if count < shortest:
                shortest = count
                end = mend
                start = mstart
        return s[start:end+1]

    def expandFromCenter(self, s, t, i):

        found_all = len(t)

        left = i
        right = i
        start = left
        end = right

        map = {}
        for l in t:
            if l in map:
                map[l] += 1
            else:
                map[l] = 1

        while (left >= 0 or right < len(s)) and found_all != 0:
            print(found_all)
            # if left a valid character in s range
            if left >= 0:
                if s[left] in map:
                    val = map[s[left]]
                    if val != 0:
                        start = left
                        found_all -= 1
                        val -= 1
                        map[s[left]] = val
                left -= 1
            # if found all characters in t
            if found_all == 0:
                break

            # if right is a valid character in s range
            if right != left and right <= len(s) - 1:
                if s[right] in map:
                    val = map[s[right]]
                    if val != 0:
                        end = right
                        found_all -= 1
                        val -= 1
                        map[s[right]] = val
                right += 1

            if found_all == 0:
                break
        return [end-start+1, start, end]

solution = Solution()
s = "sometttbsuhing b u t t s"
t= "butts"
print(solution.minWindowSubstring(s, t))
