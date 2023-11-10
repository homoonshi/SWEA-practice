T=10

for test_case in range(1,T+1):

    dump=int(input())
    box=list(map(int,input().split()))

    result=0

    while dump>0:

      box[box.index(max(box))]-=1
      box[box.index(min(box))]+=1
      dump-=1

    print(f"#{test_case}{max(box)-min(box)}")


