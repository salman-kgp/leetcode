//problem can be found here https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        seen = {}
        seen[nums[0]] = 0
        for i in xrange(1,len(nums)):
            diff = target-nums[i]
            if diff in seen:
                return [seen[diff],i]
            seen[nums[i]] = i
        return []
