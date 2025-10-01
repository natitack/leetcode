import unittest
from solution import Solution

class TestMedianTwoSortedArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # Example 1: nums1 = [1,3], nums2 = [2] -> 2.00000
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.0
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        # Example 2: nums1 = [1,2], nums2 = [3,4] -> 2.50000
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.5
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_empty_first_array(self):
        nums1 = []
        nums2 = [1, 2, 3]
        expected = 2.0
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_empty_second_array(self):
        nums1 = [1, 2, 3]
        nums2 = []
        expected = 2.0
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_single_elements(self):
        nums1 = [1]
        nums2 = [2]
        expected = 1.5
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        nums1 = [-5, -1, 0]
        nums2 = [-2, 3, 7]
        expected = -0.5
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_identical_elements(self):
        nums1 = [1, 1, 1]
        nums2 = [1, 1, 1]
        expected = 1.0
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_different_sizes(self):
        nums1 = [1, 3]
        nums2 = [2, 4, 5, 6, 7]
        expected = 4.0
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_large_numbers(self):
        nums1 = [100000]
        nums2 = [100001]
        expected = 100000.5
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()