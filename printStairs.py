
def printStairPathsUtil(ans,i,n):
    if(n<0):
      return
    if(n==0):
      ans[i]=''
      print(''.join(ans))
      return
    ans[i]='1'
    printStairPathsUtil(ans,i+1,n-1)

    ans[i]='2'
    printStairPathsUtil(ans,i+1,n-2)

def printStairPaths(n):
  ans=['']*(n+1)
  printStairPathsUtil(ans,0,n);
 

n=7
printStairPaths(n)
