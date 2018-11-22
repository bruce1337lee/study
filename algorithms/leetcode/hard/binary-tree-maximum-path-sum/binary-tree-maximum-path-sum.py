class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype int
        """
        return self.crawl(root, 0)

    def crawl(self, root, count):
        count += root.val
        leftcount = 0
        rightcount = 0
        if root.left is None and root.right is None:
            return count
        if root.left is not None:
            leftcount = self.crawl(root.left, count)
        if root.right is not None:
            rightcount = self.crawl(root.right, count)

        # return greatest count
        if rightcount + leftcount > rightcount and
            rightcount + leftcount > leftcount:
                return rightcount + leftcount
        elif rightcount > leftcount:
            return rightcount
        else:
            return leftcount

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(0)
left = TreeNode(-1)
root.left = left
right = TreeNode(2)
root.right = right
rightleft = TreeNode(4)
right.left = rightleft
rightright = TreeNode(3)
right.right = rightright

solution = Solution()
print(solution.maxPathSum(root))
