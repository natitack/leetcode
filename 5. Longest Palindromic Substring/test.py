import unittest
from solution import Solution

class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test case from example 1"""
        s = "babad"
        result = self.solution.longestPalindrome(s)
        # Both "bab" and "aba" are valid answers
        self.assertIn(result, ["bab", "aba"])
        self.assertEqual(len(result), 3)
    
    def test_example_2(self):
        """Test case from example 2"""
        s = "cbbd"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "bb")
    
    def test_single_character(self):
        """Test with single character"""
        s = "a"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "a")
    
    def test_all_same_characters(self):
        """Test with all same characters"""
        s = "aaaa"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "aaaa")
    
    def test_no_palindrome_longer_than_one(self):
        """Test with no palindrome longer than 1"""
        s = "abcd"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["a", "b", "c", "d"])
        self.assertEqual(len(result), 1)
    
    def test_entire_string_is_palindrome(self):
        """Test when entire string is a palindrome"""
        s = "racecar"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "racecar")
    
    def test_even_length_palindrome(self):
        """Test with even length palindrome"""
        s = "abccba"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "abccba")
    
    def test_odd_length_palindrome(self):
        """Test with odd length palindrome"""
        s = "abcba"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "abcba")

if __name__ == "__main__":
    unittest.main()