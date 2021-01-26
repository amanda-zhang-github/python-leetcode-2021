from typing import List


class Solution:
    # two pointer solution
    def max_area(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        left = 0
        right = len(height) - 1
        min_height = min(height[left], height[right])
        area = (right - left) * min_height

        while left < right:
            while left < right and height[left] <= min_height:
                left += 1
            if left == right:
                break
            min_height = min(height[left], height[right])
            if (right - left) * min_height > area:
                area = (right - left) * min_height

            while left < right and height[right] <= min_height:
                right -= 1
            if left == right:
                break
            min_height = min(height[left], height[right])
            if (right - left) * min_height > area:
                area = (right - left) * min_height

        return area


if __name__ == "__main__":
    solution = Solution()
    # empty input
    print(solution.maxArea([]))
    # 2 vertical lines with same heights
    print(solution.maxArea([1, 1]))
    # max width -> max area
    print(solution.maxArea([1, 2, 1]))
    # no 2 lines with none-zero height
    print(solution.maxArea([0, 2, 0]))
    # monotonic heights
    print(solution.maxArea([1, 2, 3, 4, 5, 6]))
    # max width -\-> max area
    print(solution.maxArea([3, 9, 3, 4, 7, 2, 12, 6]))
