class Solution(object):
    def countVowelStrings1(self, n):
        #dp[0][1] 表示以a开头，长度为1的字符串的数目,以此类推
        dp = [[0 for i in range(n + 1)] for j in range(5)]
        for i in range(5):
            dp[i][1] = 1

        for i in range(2,n + 1):
            for j in range(5):
                for k in range(j,5):
                    dp[j][i] += dp[k][i - 1]

        return dp[0][n] + dp[1][n] + dp[2][n] + dp[3][n] + dp[4][n]

    def countVowelStrings(self, n):
        #我们发现可以对二维数组进行优化
        dp = [1 for i in range(5)]#dp[i]表示以a开头的，进行n次迭代，表示长度为n
        for n_iter in range(1,n):
            for i in range(5):
                for j in range(i + 1,5):
                    dp[i] += dp[j]
        return dp[0] + dp[1] + dp[2] + dp[3] + dp[4]



s = Solution()
print(s.countVowelStrings(2))