class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        pre = nums[:n-k]
        last = nums[-k:]
        nums[:k] = last
        nums[k:] = pre