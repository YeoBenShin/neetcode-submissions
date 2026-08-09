class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]: # min on the right
                left = mid + 1

            else: # min on the left
                right = mid

        return nums[left]
            