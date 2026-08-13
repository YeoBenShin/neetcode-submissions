class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # starting from the beginning, mark all possible jump location
        # when checking subsequent jump position, check if reaching that jump location is possible
        length = len(nums) - 1
        jumpLoc = [0] * (length+1)
        jumpLoc[0] = 1
        for idx, i in enumerate(nums):
            if not self.markJumpLocation(idx, nums, jumpLoc):
                return False
            elif jumpLoc[length] == 1:
                return True
        return False
        
    def markJumpLocation(self, idx, nums, jumpLoc):
        # return false if cannot reach this location
        if jumpLoc[idx] == 0:
            return False
        for i in range(nums[idx]):
            if idx+i+1 >= len(nums):
                break
            jumpLoc[idx+i+1] = 1
        return True
