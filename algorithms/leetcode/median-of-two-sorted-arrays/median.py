class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = []
        length = 0
        if len(nums1) >= len(nums2):
            length = len(nums1)
        else:
            length = len(nums2)

        x = 0
        for i in range(0, length):
            if nums1[i] < nums2[x]:
                nums.append(nums1[i])
            elif nums1[i] > nums2[x]:
                nums.append(nums2[x])
                x += 1
            else:
                nums.append(nums1[x])
                nums.append(nums2[i])
                x += 1
        print(nums)

solution = Solution()
nums1 = [1,2,3]
nums2 = [4,5,6]
solution.findMedianSortedArrays(nums1, nums2)
