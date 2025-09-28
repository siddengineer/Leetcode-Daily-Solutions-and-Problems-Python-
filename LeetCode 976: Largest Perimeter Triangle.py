Problem Understanding

We are given a list of integers nums representing side lengths. We need to choose three sides that can form a triangle and have the largest perimeter.

Triangle Rule: For sides a ≤ b ≤ c, a triangle exists if:
a+b>c

If no valid triangle exists, return 0.

Algorithm (Greedy Approach)

Sort the array in descending order.
This helps because we want the largest perimeter, so we try bigger numbers first.

Check triplets from largest to smallest:

nums[i], nums[i+1], nums[i+2]


If they satisfy the triangle rule nums[i+1] + nums[i+2] > nums[i], return their sum.

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Sort descending
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
This approach is O(n log n) due to sorting and O(n) for checking triplets, which is efficient.
