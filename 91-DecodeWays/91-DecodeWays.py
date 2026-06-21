# Last Updated: 6/22/2026, 12:44:08 AM
class Solution:
    count = 0
    code = []
    memo = {}

    def dfs(self, s):
        key = s[0]

        if key in self.memo:
            self.count += self.memo[key]
            return

        before = self.count

        if s[0] == "":
            self.count += 1
            self.memo[key] = 1
            return

        # take 1 digit
        one = s[0][0]
        if one in self.code:
            temp = s.copy()
            temp.append(one)
            temp[0] = temp[0][1:]
            self.dfs(temp)

        # take 2 digits
        if len(s[0]) >= 2:
            two = s[0][:2]
            if two in self.code:
                temp = s.copy()
                temp.append(two)
                temp[0] = temp[0][2:]
                self.dfs(temp)

        self.memo[key] = self.count - before

    def numDecodings(self, s: str) -> int:
        self.count = 0
        self.memo = {}

        for i in range(1, 27):
            self.code.append(str(i))

        self.dfs([s])

        return self.count 