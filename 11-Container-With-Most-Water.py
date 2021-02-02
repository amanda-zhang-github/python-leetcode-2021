from typing import List


class Solution:
    """
    two pointer solution
    run time O(n), space O(1)
    the area is determined by width * the shorter height
    left pointer starts from head, right pointer starts from tail
    now the question is how to move the pointers
    Claim: suppose height[L] < height[R], if there is a better solution within [L, R], then [L_opt, R_opt] must in [L+1, R]
    proof: Let [L_opt, R_opt] be the optimal solution in [L, R], area_opt > area, L_opt >= L, R_opt <= R
           Assume [L_opt, R_opt] is not in [L+1, R] ==> L_opt = L, R_opt < R
           so area_opt = (R_opt - L_opt) * min(height[L_opt], height[R_opt])
                       = (R_opt - L) * min(height[L], height[R_opt])
                       < (R - L) * height[L]
                       = area
           Contradiction!
           So the optimal solution is guaranteed to be in [L+1, R], so we just need to move the pointer with shorter height
    """
    def max_area(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            if height[l] < height[r]:
                area = max(area, (r - l) * height[l])
                l += 1
            else:
                area = max(area, (r - l) * height[r])
                r -= 1
        return area


if __name__ == "__main__":
    solution = Solution()
    # empty input
    print(solution.max_area([]))
    # 2 vertical lines with same heights
    print(solution.max_area([1, 1]))
    # max width -> max area
    print(solution.max_area([1, 2, 1]))
    # no 2 lines with none-zero height
    print(solution.max_area([0, 2, 0]))
    # monotonic heights
    print(solution.max_area([1, 2, 3, 4, 5, 6]))
    # max width -\-> max area
    print(solution.max_area([3, 9, 3, 4, 7, 2, 12, 6]))
