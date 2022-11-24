# https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484731&idx=3&sn=aa642cbf670feee73e20428775dff0b5&scene=21#wechat_redirect
# 递归思路
def minDistance1(s1, s2):
    def dp(i, j):
        # 基础情形
        if i == -1:
            return j+1
        if j == -1:
            return i+1

        if s1[i] == s2[j]:
            return dp(i-1, j-1)
        else:
            return min(
                dp(i, j-1) + 1,  # 插入
                dp(i-1, j) + 1,  # 删除
                dp(i-1, j-1) + 1  # 替换
            )
    return dp(len(s1) - 1, len(s2) - 2)

# 动态规划优化


def minDistance(word1, word2):
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1)+1)]
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
    return dp[-1][-1]














