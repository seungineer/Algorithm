class Solution:
    def maxEnergyBoost(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        length = len(energyDrinkA)
        dp = [[-float("inf"),-float("inf"),-float("inf")] for _ in range(length)]
        dp[0][0] = energyDrinkA[0]
        dp[0][1] = 0
        dp[0][2] = energyDrinkB[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0] + energyDrinkA[i], dp[i-1][1] + energyDrinkA[i])
            dp[i][1] = max(dp[i-1][0], dp[i-1][2])
            dp[i][2] = max(dp[i-1][2] + energyDrinkB[i], dp[i-1][1] + energyDrinkB[i])
        answer = max(dp[-1])
        return answer