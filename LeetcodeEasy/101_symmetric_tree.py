from typing import Optional

# Given the root of a binary tree, check whether it is a mirror of itself


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isSame(root.left, root.right)

    def isSame(self, leftroot, rightroot):
        if leftroot is None and rightroot is None:
            # if both left and right root is None, returns True
            return True
        if leftroot is None or rightroot is None:
            # if one is None and the other is not None, returns False
            return False
        if leftroot.val is not rightroot.val:
            # check the values whether they are same
            return False
        # check the sub roots
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)
