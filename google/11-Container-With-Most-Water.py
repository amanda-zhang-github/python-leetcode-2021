from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        n = len(height)

        while right < n:
            right = left
            while right < n and height[right] <= height[left]:
                ++right

        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([4,2,0,3,2,5]))

