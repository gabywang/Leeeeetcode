class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                return [my_dict[nums[i]], i]
            else:
                my_dict[target - nums[i]] = i