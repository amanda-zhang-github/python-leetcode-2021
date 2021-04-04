from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = -1
        l, r = 0, len(nums)-1

        while l < r:
            total = nums[l] + nums[r]
            if total < k:
                if k - total < k - res:
                    res = total
                l += 1
            else:
                r -= 1
        return res

if __name__ == "__main__":
    s = Solution()

    print(s.twoSumLessThanK([34,23,1,24,75,33,54,8], 60))

    print(s.twoSumLessThanK([10, 20, 30], 15))

    print(s.twoSumLessThanK([], 0))