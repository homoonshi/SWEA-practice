import collections

T=int(input())

for test_case in range(1,T+1):

    num, c=map(int,input().split())
    num_list=list(map(int,str(num)))

    num_queue=collections.deque(num_list)
    max_num_list=[]
    max_index=collections.deque()

    while c>0:

        if len(num_queue)==1:
            max_num_list.append(num_queue.popleft())
            continue
        elif not num_queue:

            max_index.clear()
            max_num=max(max_num_list)

            for i in range(len(max_num_list)):
                if max_num==max_num_list[i]:
                    max_index.append(i)


            if len(max_index)>1:

                max_index1 = max_index.pop()
                max_index2 = max_index.pop()

                while c>0:
                    max_num_list[max_index1] = max_num_list[max_index2]
                    max_num_list[max_index2] = max_num
                    c -= 1
                break
            else :
                while c>0:
                    temp_num = max_num_list[len(max_num_list) - 1]
                    max_num_list[len(max_num_list) - 1] = max_num_list[len(max_num_list) - 2]
                    max_num_list[len(max_num_list) - 2] = temp_num
                    c -= 1
                break

        index=0
        max_index.clear()
        max_num=max(num_queue)

        for i in range(len(num_queue)):
            if max_num==num_queue[i]: # 리스트에서 제일 큰 숫자를 센다
                max_index.append(i)

        if 0 in max_index:
            max_num_list.append(num_queue.popleft())
            max_index.popleft()
            continue
        else :
            if len(max_index)>1 and c>=2 :
                index_len=len(max_index)
                equal_change=0

                while equal_change!=index_len:
                    min_num=10
                    for i in range(index_len):
                        min_num=min(min_num,num_queue[i])
                    min_index=num_queue.index(min_num)
                    max_temp_index=max_index.pop()
                    num_queue[max_temp_index]=num_queue[min_index]
                    num_queue[min_index]=max_num
                    equal_change+=1
                    c-=1
                    if c==0:
                        break

                for i in range(equal_change):
                    max_num_list.append(num_queue.popleft())

                continue

            if len(max_index)==1 or c==1:
                num_queue[max_index.pop()]=num_queue[0]
                num_queue[0]=max_num
                max_num_list.append(num_queue.popleft())
                c-=1
                continue


    num_queue=list(num_queue)

    num_list=max_num_list+num_queue

    result=''.join(map(str,num_list))


    print(f"#{test_case} {result}")