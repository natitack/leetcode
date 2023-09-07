"""imports type functionality """
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, 
        return indices of the two numbers such that they add up to target.
        """
        # declare constraints
        min_length: int = 2

        # create pointers marking the beginning and end of the list (largest and smallest numbers)
        smallest_num_index: int = 0
        largest_num_index: int = len(nums)

        # raise ConstraintError if length is out of bounds
        if min_length > largest_num_index:
            raise ConstraintError

        # resolve off by one error of the index
        largest_num_index -= 1

        # use enumerate() to keep track of order before sorting.
        sorted_nums: List[tuple[int, int]] = list(enumerate(nums))

        # sort the list by second value in the tuple
        sorted_nums.sort(key=lambda x: x[1])

        value, index = 1, 0

        # sum the largest and smallest number. If the sum is greater than the target, decriment the large variable
        # if the sum is lesser than the target, decriment the small  variable
        total: int = sorted_nums[largest_num_index][value] + \
            sorted_nums[smallest_num_index][value]

        while total != target:
            if total > target:
                largest_num_index -= 1
            else:
                smallest_num_index += 1

            total = sorted_nums[largest_num_index][value] + \
                sorted_nums[smallest_num_index][value]

        # if the sum is the target, return the indices as a list.
        return [sorted_nums[smallest_num_index][index], sorted_nums[largest_num_index][index]]


class ConstraintError(Exception):
    """
    input does not conform to prompt constraints
    """
    