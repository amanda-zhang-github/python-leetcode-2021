from typing import List


class Solution:
    def pour_water(self, heights: List[int], v: int, k: int) -> List[int]:
        """
        Water first drops at index K and rests on top of the highest terrain or water at that index.
        Then, it flows according to the following rules:
        - If the droplet would eventually fall by moving left, then move left.
        - Otherwise, if the droplet would eventually fall by moving right, then move right.
        - Otherwise, rise at it's current position.

        Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction.
        After V units of water fall at index K, how much water is at each index?
        问题有歧义，eventually fall by moving left 是有前提的，只能往height相等或者低的地方move，不能随便move

        :param heights: an elevation map, heights[i] representing the height of the terrain at index i
        :param v: units of water to drop
        :param k: index to pour water
        :return: how much water is at each index

        this solution takes O(vn) time and O(1) space, for each drop loop the elevation map to see where to put
        """
        n = len(heights)
        if n == 0 or k < 0 or k >= n:
            return []

        # Drop 1 unit of water each time
        for _ in range(v):
            p = k - 1
            left_min = k
            # let the droplet fall by moving left
            while p >= 0 and heights[p] <= heights[p+1]:
                if heights[p] < heights[left_min]:
                    left_min = p
                p -= 1
            # check if the droplet eventually fall to a lower level
            if heights[left_min] < heights[k]:
                heights[left_min] += 1
                continue

            # let the droplet fall by moving right
            p = k + 1
            right_min = k
            while p < n and heights[p] <= heights[p-1]:
                if heights[p] < heights[right_min]:
                    right_min = p
                p += 1
            # check if the droplet eventually fall to a lower level
            if heights[right_min] < heights[k]:
                heights[right_min] += 1
                continue

            # Otherwise, rise at it's current position.
            heights[k] += 1
        return heights


if __name__ == "__main__":
    solution = Solution()
    assert solution.pour_water([], 1, 1) == []
    assert solution.pour_water([2, 1, 1, 2, 1, 2, 2], 4, 3) == [2, 2, 2, 3, 2, 2, 2]
    assert solution.pour_water([1, 2, 3, 4], 2, 2) == [2, 3, 3, 4]
    assert solution.pour_water([3, 1, 3], 5, 1) == [4, 4, 4]
    assert solution.pour_water([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1], 2, 5) == [1, 2, 3, 4, 3, 3, 2, 2, 3, 4, 3, 2, 1]
    assert solution.pour_water([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1], 10, 2) == [4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 3, 2, 1]
