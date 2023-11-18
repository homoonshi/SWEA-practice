import collections

T=int(input())


for test_case in range(1,T+1):

    N = int(input())

    snail=[[0]*N for i in range(N)]

    r=1
    l,b,t=0,0,0

    number=1
    sub_num=1

    snail[0][0]=number

    stack=collections.deque()
    stack.append((0,1))

    while number!=N*N:
        height,width=stack.popleft()

        if r==1:
            for i in range(width,width+(N-sub_num)):
                number+=1
                snail[height][i]=number
            r=0
            b=1
            stack.append((height+1,width+(N-sub_num-1)))
            continue

        if b==1:
            if sub_num!=1:
                sub_num+=1
            for i in range(height,height+(N-sub_num)):
                number+=1
                snail[i][width]=number
            b=0
            l=1
            stack.append((height+(N-sub_num-1),width-1))
            continue

        if l==1:
            for i in range(width,width-(N-sub_num),-1):
                number+=1
                snail[height][i]=number
            l=0
            t=1
            stack.append((height-1,width-(N-sub_num-1)))
            continue

        if t==1:
            sub_num+=1
            for i in range(height,height-(N-sub_num),-1):
                number+=1
                snail[i][width]=number
            t=0
            r=1
            stack.append((height-(N-sub_num-1),width+1))
            continue

    print(f"#{test_case}")
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=" ")
        print(end="\n")

