
T=10
for test_case in range(1, T + 1):

    N = int(input())
    height = list(map(int, input().split()))

    result = 0
    v = 0

    i=2

    while i <= (N-3):

        if height[i]<=height[i+1] or height[i]<=height[i+2]:
            if height[i+1]<=height[i+2]:
                i+=2
                continue
            else :
                i+=1
                continue

        if height[i]<=height[i-2] :
            i+=3
            continue
        if height[i]<=height[i-1] :
            i+=3
            continue

        if height[i]>height[i+1] and height[i]>height[i+2]:
            v=max(height[i+1],height[i+2],height[i-1],height[i-2])
            result+=height[i]-v
            i+=3
            continue

    print(f"#{test_case} {result}")





