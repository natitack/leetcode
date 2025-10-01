import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    """
    Tests generated from prompt examples

    Given a string `s`, find the length of the longest substring 
    without duplicate characters.

    """

    def test_example_1(self):
        """
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.        
        """
        s = Solution()
        print(f"abcabcbb result: {s.longestSubstring('abcabcbb')}")
        self.assertTrue(s.longestSubstring('abcabcbb') == 3)

    def test_example_2(self):
        """
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        """
        s = Solution()
        self.assertTrue(s.longestSubstring('bbbbb') == 1)

    def test_example_3(self):
        """
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        """
        s = Solution()
        print(f"abcde result: {s.longestSubstring('pwwkew')}")

        self.assertTrue(s.longestSubstring('pwwkew') == 3)

    def test_example_4(self):
        """
        Input: s = "abcde"
        Output: 5
        Explanation: The answer is "abcde", with the length of 5.
        This tests the situation where there are no duplicates. 
        """
        s = Solution()
        print(f"abcde result: {s.longestSubstring('abcde')}")
        self.assertTrue(s.longestSubstring('abcde') == 5)

    def test__example_5(self):
        """
        Input: s = "abcabcdef"
        Expected Output: 6 (substring "abcdef")
        """
        s = Solution()
        result = s.longestSubstring('abcabcdef')
        print(f"abcabcdef result: {result} (expected: 6)")
        self.assertTrue(result == 6)

if __name__ == '__main__':
    unittest.main()