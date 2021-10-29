#https://leetcode.com/problems/coin-change/
int coinChange(int* c, int n, int a)
{
    int arr[a+1][n];
    for(int i=0;i<=a;i++)
    {
        for(int j=0;j<n;j++)
        {
            arr[i][j]=INT_MAX;
            arr[0][j]=0;
        }
    }
    for(int i=1;i<=a;i++)
    {
        for(int j=0;j<n;j++)
        {
            int x=INT_MAX,y=INT_MAX;
    
            if(i>=c[j])
            {
                if(arr[i-c[j]][j] != INT_MAX)
                    x = (arr[i-c[j]][j]+1);
            }
            if(j>0 && arr[i][j-1]!=INT_MAX) y=arr[i][j-1];
            
            arr[i][j]=y;
            if(x<arr[i][j]) arr[i][j]=x;
        }
    }
    if(arr[a][n-1] ==INT_MAX) return -1;
    return arr[a][n-1];   
}