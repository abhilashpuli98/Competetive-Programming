# Last Updated: 6/22/2026, 12:45:30 AM
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        text_idx = len(text) - 1
        pattern_idx = len(pattern) - 1

        return self.dfs({}, text, pattern, text_idx, pattern_idx)

    def dfs(self, memo, text, pattern, text_idx, pattern_idx):

        state = (text_idx, pattern_idx)

        if state in memo:
            return memo[state]

        if text_idx == -1 and pattern_idx == -1:
            memo[state] = True
            return True

        if text_idx != -1 and pattern_idx == -1:
            memo[state] = False
            return False

        if text_idx == -1 and pattern[pattern_idx] == '*':

            temp_idx = pattern_idx

            while temp_idx != -1 and pattern[temp_idx] == '*':
                temp_idx -= 2

            if temp_idx == -1:
                memo[state] = True
                return True

            memo[state] = False
            return False

        if text_idx == -1 and pattern[pattern_idx] != '*':
            memo[state] = False
            return False

        if pattern[pattern_idx] == '*':

            if self.dfs(memo, text, pattern, text_idx, pattern_idx - 2):
                memo[state] = True
                return True

            if pattern[pattern_idx - 1] == text[text_idx] or pattern[pattern_idx - 1] == '.':

                if self.dfs(memo, text, pattern, text_idx - 1, pattern_idx):
                    memo[state] = True
                    return True

        if pattern[pattern_idx] == '.' or pattern[pattern_idx] == text[text_idx]:

            if self.dfs(memo, text, pattern, text_idx - 1, pattern_idx - 1):
                memo[state] = True
                return True

        memo[state] = False
        return False