class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

"""
1.将每一个nums[i]的值，看成是存放前面相邻的和大于0的序列 满足题意的答案。
2.通过for i in range(1, len(nums)): 遍历数据，纠正错误存放的值
3.遍历之后nums[i]中的每一个数存放的都将是序号i前面相邻数据的“最大和”（当前面的相邻数和小于0时，存放的就是当前值numsi）
"""