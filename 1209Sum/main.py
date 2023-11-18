

T = 10

for test_case in range(1,T+1):

    t=int(input())
    num=[]
    result=0
    width=[0 for i in range(100)]
    height=[0 for i in range(100)]
    diagonal=[0,0]

    for i in range(0,100):
        num.append(list(map(int,input().split())))

    for m in range(0,100):
        for n in range(0,100):
            height[n]+=num[m][n]
            width[m]+=num[m][n]
            if m==n:
                diagonal[0]+=num[m][n]
            if m+n==100:
                diagonal[1]+=num[m][n]


    result=max(max(height),max(width),max(diagonal))


    print(f"#{t} {result}")