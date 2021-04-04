from typing import List
import sys

class Solution:  
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        pointer solution - extend from three sum
        3 sum 的一般解法有:
        - sort and two pointer
        - hash table to store value to index map

        Here we cannot use the hash map solution as we don't have a specific value to loop up

        do not stop except we find the extact match

        memory: O(log n) to O(n) depends on the implementation of the sorting algorightm, can reduce to O(1) if use selection sort
        run time: O(n^2) = sort + two pointer loop = O(nlogn) + O(n^2)
        """
        nums.sort()
        
        n = len(nums)
        diff = float('inf')
        
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(diff):
                    diff = total - target

                if diff == 0:
                    return target
                elif total < target:
                    l += 1
                else:
                    r -= 1

        return target + diff


if __name__ == "__main__":
    s = Solution()

    print(s.threeSumClosest([-1, 2, 1, -4], 1))

    print(s.threeSumClosest([1, 2, 5, 10, 11], 12))