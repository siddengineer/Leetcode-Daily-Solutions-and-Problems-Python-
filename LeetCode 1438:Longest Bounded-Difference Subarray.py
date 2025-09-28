Problem Statement

Input:

An integer array nums[].

An integer limit (non-negative).

Task:
Find the length of the longest contiguous subarray such that the absolute difference between the maximum and minimum elements in the subarray is ≤ limit.

Example 1:

Input: nums = [8, 2, 4, 7], limit = 4
Output: 2
Explanation: Subarray [2,4] or [4,7] satisfies max-min <= 4


Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: Subarray [2,4,7,2] satisfies max-min <= 5

Algorithm (Sliding Window + Deques)

Initialize:

start = 0 → start index of current window

max_len = 0 → maximum subarray length

Two deques:

max_dq → decreasing order, stores indices of current max candidates

min_dq → increasing order, stores indices of current min candidates

Iterate through array (end pointer):

Update max_dq: remove elements smaller than nums[end] from the back, then append end.

Update min_dq: remove elements larger than nums[end] from the back, then append end.

Check window validity:

While nums[max_dq[0]] - nums[min_dq[0]] > limit:

Move start forward by 1.

Remove indices from front of deques if they are out of the window (< start).

Update max length:

max_len = max(max_len, end - start + 1)

Return:
max_len → length of the longest valid subarray


from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        max_dq = deque()
        min_dq = deque()
        start = 0
        max_len = 0

        for end in range(len(nums)):
            while max_dq and nums[end] > nums[max_dq[-1]]:
                max_dq.pop()
            max_dq.append(end)

            while min_dq and nums[end] < nums[min_dq[-1]]:
                min_dq.pop()
            min_dq.append(end)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                start += 1
                if max_dq[0] < start:
                    max_dq.popleft()
                if min_dq[0] < start:
                    min_dq.popleft()

            max_len = max(max_len, end - start + 1)

        return max_len
Complexity	Explanation
Time: O(n)	Each element is added and removed from max_dq and min_dq at most once.
Space: O(n)	Two deques may store indices of all elements in the worst case.


