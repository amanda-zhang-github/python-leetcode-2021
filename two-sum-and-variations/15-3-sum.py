from collections import OrderedDict
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        original solution
        run time O(n^2) = create orderedDict O(nlogn) + loop a and b O(n^2)
        memory O(n): OrderedDict to track frequency of item in input list
        """
        triples = []
        value_to_count = OrderedDict()
        for num in nums:
            value_to_count[num] = value_to_count.get(num, 0) + 1

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
    solution = Solution()
    print(solution.three_sum([-1, 0, 1, 2, -1, -4]))

    # empty input
    print(solution.three_sum([]))
    # input size less than 3
    print(solution.three_sum([1, 1]))
    # input size larger than 3, but no such triplet
    print(solution.three_sum([1, 1, 0]))
    # input with distinct numbers
    print(solution.three_sum([-1, 0, 1, 2]))
    # input with duplicate numbers
    print(solution.three_sum([-1, -1, 0, 0, 0, 1, 2]))