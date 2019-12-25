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
                        nums_dict[item] = idx # since there is only one solution, store only the latest index for a repeated item

                for idx, item in enumerate(nums):
                        second_item = target - item
                        if second_item in nums_dict:
                                if idx != nums_dict[second_item]: # only if second_item is not the same as item (can happen when for e.g. target is 6 and array is [3,2,4])
                                       return [idx, nums_dict[second_item]]

obj = Solution()
print obj.twoSum([2,7,11,15], 9)
print obj.twoSum([3,2,4], 6)
