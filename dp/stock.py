#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def maxProfit(self, p: List[int]) -> int:
        """
            2 tr*len
            tr,i=mx(tr,i-1 or p[i]-p[j]+tr-1,j-1)
        """
        dp=[[0]*(len(p)) for _ in range(3)]
        
        for k in range(1,3):
            mi=p[0]
            for i in range(1,len(p)):
                mi=min(mi,p[i]-dp[k-1][i-1])
                dp[k][i]=max(dp[k][i-1],p[i]-mi)
        print(dp)
        return dp[-1][-1]
            