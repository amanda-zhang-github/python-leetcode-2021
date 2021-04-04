from collections import OrderedDict
from typing import List

"""
LC 15 Find all unique triplets in the array which gives the sum of zero.
Assumption:
1. such tripe might not exist
2. can be multiple triples
"""


class ThreeSum:
    """
    Sort solution

    2-sum要求return index, 因此不能sort，因为那样会破坏position; 且因为return的是index, 就算有多个解也不会重复
    但是3-sum要求return的是value，因此可以sort，且要注意value triples can have duplicates, need to make sure to eliminate duplicates
    a + b + c = 0 <==> b + c = -a 因此对每个a, 找b, c可以用2-sum-II

    run time: O(n^2), memory O(1)
    """
    @staticmethod
    def three_sum_sort(nums: List[int]) -> List[List[int]]:
        triples = []
        nums.sort()

        for i in range(len(nums)):
            # improvement: nums已经sort过，nums[i]是三个数里最小的，最小的都大于0，那么和不可能为零就不用往下看了
            # 只在target sum为0时才有用
            if nums[i] > 0:
                break
            # avoid duplicate的关键是: move pointer to the next different number
            if i == 0 or nums[i-1] != nums[i]:
                pairs = ThreeSum.two_sum_sort(nums, -nums[i], i + 1)
                triples.extend([[nums[i], pair[0], pair[1]] for pair in pairs])

        return triples
    """
    Extension of TwoSum.two_sum_III_sort by adding start index, can start finding two sum from any index
    """
    @staticmethod
    def two_sum_sort(nums: List[int], target: int, start: int) -> List[List[int]]:
        pairs = []
        l, r = start, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                # can have multiple solutions, should not stop after finding one
                pairs.append([nums[l], nums[r]])
                l += 1
                r -= 1
                # increment l to the next different number to avoid duplicate
                # nums[l] different && nums[l] + nums[r] = -a -> nums[r] different
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif total < target:
                l += 1
            else:
                r -= 1
        return pairs

    @staticmethod
    def three_sum_unsort(self, nums: List[int]) -> List[List[int]]:
        """
        original solution
        run time O(n^2) = create orderedDict O(nlogn) + loop a and b O(n^2)
        memory O(n): OrderedDict to track frequency of item in input list
        """
        triples = []
        value_to_count = {}
        for num in nums:
            value_to_count[num] = value_to_count.get(num, 0) + 1
        value_to_count.keys()

        for a in value_to_count:
            value_to_count[a] = value_to_count.get(a) - 1
            for b in value_to_count:
                if b >= a and value_to_count[b] > 0:
                    value_to_count[b] = value_to_count.get(b) - 1
                    c = -a-b
                    if c >= b and value_to_count.get(c, 0) > 0:
                        triples.append([a, b, c])
                    value_to_count[b] = value_to_count.get(b) + 1
            value_to_count[a] = value_to_count.get(a) + 1

        return triples


if __name__ == "__main__":
    solution = ThreeSum()
    print(solution.three_sum_sort([-1, 0, 1, 2, -1, -4]))

    # empty input
    print(solution.three_sum_sort([]))
    # input size less than 3
    print(solution.three_sum_sort([1, 1]))
    # input size larger than 3, but no such triplet
    print(solution.three_sum_sort([1, 1, 0]))
    # input with distinct numbers
    print(solution.three_sum_sort([-1, 0, 1, 2]))
    # input with duplicate numbers
    print(solution.three_sum_sort([-1, -1, 0, 0, 0, 1, 2]))
