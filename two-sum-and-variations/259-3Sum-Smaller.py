from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        和3sum cloest不同，这题要求
        find the number of index triplets such that the sum is less than the target

        two pointer solution: run time O(n^2), memory O(1)
        """
        count = 0
        n = len(nums)
        nums.sort()

        for i in range(0, n-2):
            l, r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                """
                fix index i, if nums[i] + nums[l] + nums[r] < target
                then any triplet (i, l, r') s.t l < r' <= r satisfies nums[i] + nums[l] + nums[r'] < target
                there are r - (l+1) + 1 = r - l of r'
                """
                if total < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumSmaller([-2, 0, 1, 3], 2))

    print(s.threeSumSmaller([6, -1, -4, 3, 1, 1], 1))

    print(s.threeSumSmaller([], 2))

    print(s.threeSumSmaller([1], 2))


