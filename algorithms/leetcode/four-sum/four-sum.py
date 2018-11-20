class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[List[int]]
        """
        # num -> True / False
        num_added = {} # maybe???
        three_sums_map = {}

        #
        four_sums = []

        # all unique three sums
        # sum -> [num1, num2, num3]
        three_sums = {}

        # create all unique combinations of 3
        # store there sums as the key
        # there value in an array of their indices

        for i in range(0, len(nums)):
            for x in range(i+1, len(nums)):
                for y in range(x+1, len(nums)):
                    if x != y & y != i & x != i:
                        three_sum = nums[i] + nums[x] + nums[y]
                        if three_sum in three_sums:
                            three_sums[three_sum].append([nums[i],
                                                          nums[x], nums[y]])
                        else:
                            three_sums[three_sum] = [[nums[i], nums[x],
                                                     nums[y]]]

        for i in nums:
            complement = target - i
            if complement in three_sums:
                sums = three_sums[complement]
                sum_group = []
                for sum in sums:
                    sum.append(i)
                    sum_group.append(sum)
                return sum_group

solution = Solution()
nums = [5,1,1,1,1,1,1]
target = 8


print(solution.fourSum(nums, target))
