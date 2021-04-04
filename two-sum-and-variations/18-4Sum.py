from typing import List

def four_sum_1(nums: List[int], target: int) -> List[List[int]]:
    """
    run time: two sum O(n), three sum O(n^2), four sum (O(n^3))
    space: O(1) depends on how the sort is implemented
    """
    quadruplets = []
    nums.sort()
    n = len(nums)

    i = 0
    while i < n-3:
        if nums[i] > target/4:
            return quadruplets

        j = i+1
        while j < n-2:
            low, high = j+1, n-1
            while low < high:
                total = nums[i] + nums[j] + nums[low] + nums[high]
                if total == target:
                    quadruplets.append([nums[i], nums[j], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low-1] == nums[low]:
                        low += 1
                elif total < target:
                    low += 1
                else:
                    high -= 1

            j += 1
            while j < n-2 and nums[j-1] == nums[j]:
                j += 1
        i += 1
        while i < n-3 and nums[i-1] == nums[i]:
            i += 1

    return quadruplets

"""
在写过了2sum, 3sum, 4sum之后我们可以给出一个k sum 的通用解

Assumption: 
1. nums is sorted
2. k >= 2

run time: O(n^k-1) + O(nlogn) 其中O(nlogn)是sort需要的时间 k > 2时, sort需要的时间不影响time complexity
memory: O(k) recursion需要的时间
"""
def k_sum(nums: List[int], target: int, k: int) -> List[List[int]]:
    n = len(nums)
    res = []

    # nums is sorted, so nums[i]*k > target ==> k sum > target
    if n == 0 or nums[0] * k > target:
        return res

    if k == 2:
        l, h = 0, n-1
        while l < h:
            total = nums[l] + nums[h]
            if total == target:
                res.append([nums[l], nums[h]])
                l += 1
                h -= 1
                while l < h and nums[l-1] == nums[l]:
                    l += 1
            elif total < target:
                l += 1
            else:
                h -= 1
        return res

    i = 0
    while i <= n-k:
        k_minus_one_sums = k_sum(nums[i+1:], target-nums[i], k-1)
        res.extend([[nums[i]] + x for x in k_minus_one_sums])
        i += 1
        while i <= n-k and nums[i-1] == nums[i]:
            i += 1
    return res


def four_sum_2(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    return k_sum(nums, target, 4)


if __name__ == "__main__":
    print(four_sum_2([1, 0, -1, 0, -2, 2], 0))

    print(four_sum_2([1, 1, 1], 0))

    print(four_sum_2([], 0))
