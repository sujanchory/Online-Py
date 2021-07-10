class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        y=x
        if x<0:
            x=abs(x)
        while x!=0:
            r=x%10
            x=x//10
            rev=rev*10+r
        if rev>(2**31):
            return 0                
        else:
            if y<0:
                return -(rev)
            else:
                return rev
        

        
        
