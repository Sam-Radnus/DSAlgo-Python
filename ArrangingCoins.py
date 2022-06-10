#here we are trying to find the first row where the number of coins is closest to  n
#we are trying to find the largest sum
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left,right=0,n
        k,sum=0,0
        while left<=right:
            k=(left+right)//2
            sum=(k*(k+1))//2
            if sum==n:#if all the rows are complete
                return int(k)
            if sum<n:
               left=k+1
            else:
                right=k-1
        return right