import collections

T=int(input())


for test_case in range(1,T+1):

    N = int(input())

    snail=[[0]*N for i in range(N)]

    r,l,b,t=1,0,0,0
    number=1

    stack=collections.deque()
    stack.append((0,0))
    snail[0][0]=1

    while number is not N*N:

        length,width=stack.popleft()
        number+=1

        if r==1 and width<N-1:
            if snail[length][width+1]!=0:
                r=0
                b=1
                snail[length+1][width]=number
                stack.append((length+1,width))
                continue

            snail[length][width+1]=number
            stack.append((length,width+1))
            continue
        if r==1 and width==N-1:
            r=0
            b=1
            snail[length+1][width]=number
            stack.append((length+1,width))
            continue

        if b==1 and length<N-1:
            if snail[length+1][width]!=0:
                b=0
                l=1
                snail[length][width-1]=number
                stack.append((length,width-1))
                continue

            snail[length+1][width]=number
            stack.append((length+1,width))
            continue
        if b==1 and length==N-1:
            b = 0
            l = 1
            snail[length][width - 1] = number
            stack.append((length, width - 1))
            continue

        if l==1 and width<N-1:
            if snail[length][width-1]!=0:
                l=0
                t=1
                snail[length-1][width]=number
                stack.append((length-1,width))
                continue

            snail[length][width-1]=number
            stack.append((length,width-1))
            continue
        if l==1 and width==N-1:
            l = 0
            t = 1
            snail[length - 1][width] = number
            stack.append((length - 1, width))
            continue

        if t==1 and length<N-1:
            if snail[length-1][width]!=0:
                t=0
                r=1
                snail[length][width+1]=number
                stack.append((length,width+1))
                continue

            snail[length-1][width]=number
            stack.append((length-1,width))
            continue
        if t==1 and length==N-1:
            t=0
            r=1
            snail[length-1][width]=number
            stack.append((length-1,width))
            continue

    print(f"#{test_case}")
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=" ")
        print(end="\n")
