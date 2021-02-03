from typing import List


class Solution:
    """
    Brute force solution that takes O(n^2) time

    total water = 0
    for i = 1 : n
        Let left_max(i) = height of the tallest building on the left side of i
                        = max(H[0], ..., H[i])
            right_max(i) = height of the tallest building on the right side of i
                         = max(H[i], ..., H[n-1])
        level of trapped water at i = min(left_max(i), right_max(i))
        w_i (trapped water at i) = min(left_max(i), right_max(i)) - H[i]
        total water += w_i

    return total water
    ---------------------------------------------------------------------------------------
    Is there a better way to update left_max(i) and right_max(i)?

    2 pointers solution: run time O(n), space O(1)
    Let left pointer L starts from head, right pointer R starts from tail (L < R)

    suppose height[L] < height[R]
        left_max(L) = max(left_max(L-1), height[L])
        since right_max[L] >= right_max[R] >= height[R], we have w_L = min(left_max(L), right_max(L)) - H[i] = left_max(L) - H[i]
        as we've known w_L, we can move to L+1

    suppose height[L] >= height[R]
        right_max(R) = max(right_max(R+1), height[R])
        since left_max[R] >= left_max[L] >= height[L], we have w_R = min(left_max(R), right_max(R)) - H[i] = right_max(R) - H[i]
        as we've known w_R, we can move to R-1

    We can update left_max(L) and right_max(R) in O(1) if we track left_max(L-1) and right_max(R+1)
    """
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        volume = 0
        left_max = 0
        right_max = 0

        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                volume += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                volume += right_max - height[r]
                r -= 1
        return volume


if __name__ == "__main__":
    solution = Solution()
    # smallest height in the middle
    assert solution.trap([4, 2, 0, 3, 2, 5]) == 9

    # largest height in the middle
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    # monotonic increasing heights -> no water trapped
    assert solution.trap([1, 2, 3, 4, 10]) == 0

    # monotonic decreasing heights -> no water trapped
    assert solution.trap([10, 8, 6, 5]) == 0

    # empty heights -> no water trapped
    assert solution.trap([]) == 0

    # all 0 heights -> no water trapped
    assert solution.trap([0, 0]) == 0





