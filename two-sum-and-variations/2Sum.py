from typing import List
from collections import OrderedDict

"""
2-sum是3-sum的基础
- two_sum_III_sort是three_sum_sort的基础
- two_sum_III_unsort是three_sum_unsort的基础
"""


class TwoSum:
    """
    LC 1 最基本的 two sum

    Assumption: there is exactly one solution, so we don't need to deal with the duplication in the result

    optimal solution: one pass hash table
    run time O(n), space O(n)
    idea: for each number x, find its complementary (target - x). If complementary already exists in the look up table, return index
          otherwise add x into the look up table to be used as other number's complementary
    """
    @staticmethod
    def two_sum_I(nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        result = []
        for index, x in enumerate(nums):
            if target - x in num_to_index:
                result = [num_to_index.get(target-x), index]
            else:
                num_to_index[x] = index
        return result

    """
    LC 167
    
    Assumption: there is one unique solution, so we don't need to deal with the duplication in the result
                the input numbers are sorted in ascending order
    run time O(n), space O(1)
    如果input没有order的话就要花O(nlogn)来sort， total run time is O(nlogn)
    idea: let L starts from 0, R starts from len - 1. 
          if nums[L] + nums[R] == target, return
          else if nums[L] + nums[R] < target, L++
          else R--
          
    Pf: assume {L*, R*} is the solution
        because the 2 pointers moves from the boundary to the center, at some point, one of them will first reach the solution
        w.l.o.g, assume L reaches L* first, then 
          nums[L] + nums[R] = nums[L*] + nums[R] >= nums[L*] + nums[R*] > target
        according to the idea, we will move R to R-1 recursively, so eventually will reach R*
    """
    @staticmethod
    def two_sum_II(nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                return [l, r]
            elif total < target:
                l += 1
            else:
                r -= 1
        return None

    # ========================================================================
    """ 
    Find all unique pairs in the array which gives the sum of the target. 
    Leetcode 上没有，是以上case的general，也是3-sum的基础
    Assumption:
    1. such pair might not exist
    2. can have duplicate solutions, but need to eliminate duplicates in the return result
    3. 要求return value
    
    As there can be multiple solutions, should not stop after finding one solution
    """

    """
    If we can sort the input array
    run time: O(nlogn), space O(1)
    """
    @staticmethod
    def two_sum_III_sort(nums: List[int], target: int) -> List[List[int]]:
        pairs = []
        nums.sort()
        l, r = 0, len(nums)-1
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                pairs.append([nums[l], nums[r]])
                l += 1
                r -= 1
                # increment l to the next different number to avoid duplicate
                # nums[l] different && nums[l] + nums[r] = -a -> nums[r] different
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif total < target:
                l += 1
            else:
                r -= 1
        return pairs

    """
    如果input array不可以sort的话，那就用hash table来记录value -> count, 如果count > 0, 说明value还没被用过，否则就是已经和之前的number组成pair了
    run time: O(n), space O(n)
    """
    @staticmethod
    def two_sum_III_unsort(nums: List[int], target: int) -> List[List[int]]:
        pairs = set()
        value_to_count = {}
        for num in nums:
            complementary = target - num
            # if the complementary number has been seen and hasn't been used (means same solution hasn't been added)
            count = value_to_count.get(complementary, 0)
            if count > 0:
                # sort the pair to ensure [1, 2], [2, 1] is regarded as the same in set
                pairs.add(sorted([num, complementary]))
                # mark complementary as used
                value_to_count[complementary] = count - 1
            else:
                # add num to be used later
                value_to_count[num] = value_to_count.get(num, 0) + 1
        return list(pairs)


if __name__ == "__main__":
    print(TwoSum.two_sum([2, 7, 11, 15], 9))
    print(TwoSum.two_sum([3, 2, 4], 6))
    print(TwoSum.two_sum([3, 3], 6))
