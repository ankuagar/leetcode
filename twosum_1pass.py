class Solution(object):
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        Example:
                Given nums = [2, 7, 11, 15], target = 9,
                Because nums[0] + nums[1] = 2 + 7 = 9,
                return [0, 1].
        """
        def twoSum(self, nums, target):
                """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
                """
                nums_dict = {}
                for idx,item in enumerate(nums):
                        if target - item in nums_dict:
                                return [nums_dict[target - item], idx]
                        else:                                                
                                nums_dict[item] = idx


obj = Solution()
print obj.twoSum([2,7,11,15], 9)
print obj.twoSum([3,2,4], 6)
