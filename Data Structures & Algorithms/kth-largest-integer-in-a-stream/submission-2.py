import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums        

    def add(self, val: int) -> int:
        self.nums.append(val)
        heap_list = []
        idx = 0
        while idx < self.k:
            heapq.heappush(heap_list, self.nums[idx])
            idx += 1
        
        while idx < len(self.nums):
            if self.nums[idx] > heap_list[0]: # bigger than the current kth largest element
                heapq.heapreplace(heap_list, self.nums[idx])
            idx += 1
        
        return heapq.heappop(heap_list)
