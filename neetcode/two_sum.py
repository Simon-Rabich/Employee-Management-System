from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen_map:
                return [i, seen_map[diff]]
            seen_map[num] = i



class Solution2:
    def two_sum_two(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            cur_sum = nums[l] + nums[r]

            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]


class Sol3:
    def is_palindrome(self, txt: str) -> bool:
        l, r = 0, len(txt) - 1
        while l < r:
            if txt[l] != txt[r]:
                return False
            l += 1
            r -= 1
        return True



    def pali(self):

class Sol4:
    def