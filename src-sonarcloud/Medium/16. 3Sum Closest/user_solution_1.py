class Solution:
    def threeSumClosest(self, a: List[int], x: int) -> int:
        
        def find(i,j,k):
            if i>=j:
                return 
            s=a[i]+a[j]+a[k]
            if s>=t[0]:
                find(i,j-1,k)
            elif s<t[1]:
                find(i+1,j,k)
            else:
                t[0]=x+abs(s-x)
                t[1]=x-abs(s-x)
                res[0]=s
                find(i+1,j,k)
                find(i,j-1,k)
                
        
        n=len(a)
        a.sort()
        res=[0]
        t=[math.inf,-math.inf]
        for k in range(n-2):
            i=k+1
            j=n-1
            find(i,j,k)
        return res[0]
