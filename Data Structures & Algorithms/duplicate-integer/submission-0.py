class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = dict()
        for num in nums:
            if num not in history:
                history[num] = 1
            else:
                return True
        return False
        