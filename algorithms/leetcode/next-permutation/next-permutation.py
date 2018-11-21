class Solution(object):
    def nextPermutation(self, nums):
        """
        :type numes: List[int]
        :rtype: void, Don't return anyting modify nums
        """
        i = 0
        while i < len(nums)-1:
            next_greatest_ind = 0
            if nums[i] > nums[i+1]:
                # index of number closest to the end of the array
                # which is less than nums[i]
                next_greatest_ind = i+1
                x = i + 1
                while x < len(nums):
                    if nums[i] > nums[x]:
                        next_greatest_ind = x
                    if nums[x] > nums[i]:
                        i = x
                        next_greatest_ind = -1
                        break
                    x += 1
                if next_greatest_ind > - 1:
                    temp = nums[i]
                    nums[i] = nums[next_greatest_ind]
                    nums[next_greatest_ind] = temp
                    print(nums)
        # everything is in ascending order
        if next_greatest_ind == 0:


            i += 1
        return

solution = Solution()
nums = [3,2,1]
solution.nextPermutation(nums)
print(nums)
