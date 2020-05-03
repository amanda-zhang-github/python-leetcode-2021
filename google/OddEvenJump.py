from typing import List

# 我一开始的想法是
# 假设当前在index i, 如果下一步是odd jump，那么先找出next index j，然后i是否可以走到最后可以由以下公式表达
# is_good_odd[i] = False, if j == n
#                  is_good_even[j], if j < n
#
# 同理如果下一步是even jump，则有
# is_good_even[i] = False, if j == n
#                  is_good_odd[j], if j < n
#
# 因为j > i，为了使用这个DP公式应该由bottom up算is_good_even和is_good_odd
# 这里解法大致上是对的，但是当A很大的时候exceed time limit。所以我们先分析以下这个解法的complexity
# 对于每一个i, loop i到n-1来找下一步的位置j， 找到之后用O(1)的时间算出 is_good_odd[i] 和 is_good_even[i]
# 所以总共的time complexity是O(n^2)
# memory usage = O(n)， 因为is_good_odd和is_good_even各用了n

# ==================================================================
# 为了降低complexity，只需要改进"对于每一个i, loop i到n-1来找下一步的位置j"这个部分
#
# 可以提前遍历一遍这个list，对于每个点找出它下一个odd jump的位置和even jump的位置
# odd jump的位置可有如下方法找出
# 首先把A从大到小sort，然后记住sort完的结果对应的A中的index
# A = [5, 1, 3, 4, 2] ==> A[1] < A[4] < A[2] < A[3] < A[0]
# 因此我们有[1, 4, 2, 3, 0]
# 遍历这个list可知
# - 在index 1往后看比A[1]大的最小的value在A[4]，所以从index 1 odd jump的话会到A[4]
# - 4已经是最后一个
# - 在index 2之后比它大的最小的value在A[3], 所以从index 2 odd jump的话会落到A[3]
# - index[0]比index[3]大，但是0在3前面，所以index 3 没有下一步了
# 这个逻辑可以用下面的method表达

# def find_odd_jump_destination(A: List[int]):
#     indexOrder = sorted(range(len(A)), key=lambda i: A[i])
#     toIndex = [None] * len(A)
#
#     stack = []  # save indexes that have looped and has not been assign "to index"
#     for i in indexOrder:
#         # 有index没有找到下一步，且index i是第一个存的值比之前有没有没有找到下一步的都要大
#         # 那么stack里的index都应该jump到index
#         while stack and i > stack[-1]:
#             toIndex[stack.pop()] = i
#         # 都jump到index i， 下一步怎么走还不知道，先存起来
#         stack.append(i)
#     return toIndex

# find_even_jump_destination 和上面的唯一区别就是indexOrder应该按照A的值descending order来排
# 即 indexOrder = sorted(range(len(A)), key=lambda i: -A[i])
# time complexity = O(nlogn) + O(n) = O(nlogn)
# O(nlogn) is for sorting

class Solution:
    def find_odd_jump_destination(A: List[int]):
        indexOrder = sorted(range(len(A)), key=lambda i: A[i])
        toIndex = [None] * len(A)

        stack = []  # save indexes that have looped and has not been assign "to index"
        for i in indexOrder:
            # 有index没有找到下一步，且index i是第一个存的值比之前有没有没有找到下一步的都要大
            # 那么stack里的index都应该jump到index
            while stack and i > stack[-1]:
                toIndex[stack.pop()] = i
            # 都jump到index i， 下一步怎么走还不知道，先存起来
            stack.append(i)
        return toIndex

    def find_even_jump_destination(A: List[int]):
        indexOrder = sorted(range(len(A)), key=lambda i: -A[i])
        toIndex = [None] * len(A)

        stack = []  # save indexes that have looped and has not been assign "to index"
        for i in indexOrder:
            # 有index没有找到下一步，且index i是第一个存的值比之前有没有没有找到下一步的都要大
            # 那么stack里的index都应该jump到index
            while stack and i > stack[-1]:
                toIndex[stack.pop()] = i
            # 都jump到index i， 下一步怎么走还不知道，先存起来
            stack.append(i)
        return toIndex

    def odd_even_jumps(self, A: List[int]) -> int:
        n = len(A)
        is_good_odd = [False] * n
        is_good_even = [False] * n

        # last index in A is always a good start
        is_good_odd[-1] = True
        is_good_even[-1] = True

        nextIdx_odd = self.find_odd_jump_destination(A)
        nextIdx_even = self.find_even_jump_destination(A)

        for i in range(n - 2, -1, -1):
            nextIdx = n
            # if current jump is odd jump
            nextIdx = nextIdx_odd[i]  # None means can't jump any more
            if nextIdx:
                is_good_odd[i] = is_good_even[nextIdx]

            # if current jump is even jump
            nextIdx = nextIdx_even[i]
            if nextIdx:
                is_good_even[i] = is_good_odd[nextIdx]

        return sum(is_good_odd)


if __name__ == "__main__":
    s = Solution()
    print(s.odd_even_jumps([10, 13, 12, 14, 15]))
    print(s.odd_even_jumps([2, 3, 1, 1, 4]))
    print(s.odd_even_jumps([5, 1, 3, 4, 2]))
    print(s.odd_even_jumps([1, 2, 3, 2, 1, 4, 4, 5]))
