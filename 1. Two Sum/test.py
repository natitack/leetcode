import unittest
from solution import Solution
from solution import ConstraintError


class TestSolution(unittest.TestCase):
    """
    Tests generated from prompt examples

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order. 
    """

    def test_example_1(self):
        """
        Input: nums = [2,7,11,15], target = 9 Output: [0,1]
        """
        s = Solution()
        self.assertTrue(sorted(s.twoSum([2, 7, 11, 15], 9)) == [0, 1])

    def test_example_2(self):
        """
        Input: nums = [3,2,4], target = 6
        """
        s = Solution()
        self.assertTrue(sorted(s.twoSum([3, 2, 4], 6)) == [1, 2])

    def test_example_3(self):
        """
        Input: nums = [3,3], target = 6 Output: [0,1]
        """
        s = Solution()
        self.assertTrue(sorted(s.twoSum([3, 3], 6)) == [0, 1])

    def test_constraints(self):
        """
        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        """
        s = Solution()
        # raise error if nums length is less than two
        self.assertRaises(ConstraintError, s.twoSum, [2], 9)
        # raise error if number is below range
        self.assertRaises(ConstraintError, s.twoSum, [2, 3, 24, -110], 9)
        # raise error if number is above range
        self.assertRaises(ConstraintError, s.twoSum, [2, 3, 24, -110], 9)
        # raise error if target is below range
        self.assertRaises(ConstraintError, s.twoSum, [2, 3, 24], -110)
        # raise error if target is above range
        self.assertRaises(ConstraintError, s.twoSum, [2, 3, 24], 110)


if __name__ == '__main__':
    unittest.main()
