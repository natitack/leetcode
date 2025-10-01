class Solution:
    def longestSubstring(self, input_string):
        current_substring = ""
        longest_substring = ""


        for each in input_string:
            if each not in current_substring:
                current_substring = current_substring + each
            elif len(current_substring) > len(longest_substring):
                longest_substring = current_substring
                current_substring = each
            else:
                current_substring = each
        return len(longest_substring)
