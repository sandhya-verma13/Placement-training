class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        s=[]
        for i in range(1,n+1):
            a=1
            y=[]
            for j in range(1,i+1):
                y.append(a)
                a=a*(i-j)//j
                print(a)
            s.append(y)
        return s
