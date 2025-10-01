class Solution:
    def longestSubstring(self, input_string):
        current_substring = ""
        substringlist = []

        for each in input_string:
            if each not in current_substring:
                current_substring = current_substring + each
            else:
                substringlist.append(current_substring)
                current_substring = each
        substringlist.append(current_substring)
        substringlist.sort(key=len, reverse=True)
        return len(substringlist[0])

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubstring("abcabcdef"))