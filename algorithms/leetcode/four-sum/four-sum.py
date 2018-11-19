class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[List[int]]
        """
        # num -> True / False
        num_added = {} # maybe???
        # sum -> [index1, index2, index3]
        three_sums_map = {}

        #
        four_sums = []

        # create all unique combinations of 3
        # store there sums as the key
        # there value in an array of their indices

        for i in range(0, len(nums)):
            for x in range(i+1, len(nums)):
                for y in range(x+1, len(nums)):
                    three_sum = nums[i] + nums[x] + nums[y]
                    if three_sum in three_sums_map:
                        sum_group = three_sums_map[three_sum]
                        sum_group.append([i, x, y])
                        three_sums_map[three_sum] = sum_group
                    else:
                        three_sums_map[three_sum] = [[i, x, y]]

        for i in nums:
            complement = target - i
            if complement in three_sums_map:
                three_sums = three_sums_map[complement]
                for sums in three_sums:
                    if sums != None:
                        three_sum_nums = [nums[sums[0]], nums[sums[1]], nums[sums[2]]]
                        sum_group.append(three_sum_nums.append(i))

        return sum_group



solution = Solution()
nums = [1,2,3,4,5,6,7,1]
target = 14

print(solution.fourSum(nums, target))
