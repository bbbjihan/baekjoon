import sys

N = int(sys.stdin.readline())
min_heap = ['trash']

def insert(num):
    min_heap.append(num)
    if len(min_heap)>2:
        ptr = len(min_heap)-1
        parent_ptr = ptr//2
        while min_heap[parent_ptr]>min_heap[ptr]:
            min_heap[parent_ptr], min_heap[ptr] = min_heap[ptr], min_heap[parent_ptr]
            ptr = parent_ptr
            if ptr == 1:
                break
            parent_ptr = ptr//2
    else:
        return

def delete():
    min_heap[1],min_heap[len(min_heap)-1] = min_heap[len(min_heap)-1],min_heap[1]
    print(min_heap.pop())
    parent_ptr = 1
    while 1:
        ptr = parent_ptr*2
        if ptr < len(min_heap)-1 and min_heap[ptr] > min_heap[ptr+1]:
            ptr+=1
        elif ptr >= len(min_heap) or min_heap[ptr] > min_heap[parent_ptr]:
            break
        min_heap[ptr], min_heap[parent_ptr] = min_heap[parent_ptr], min_heap[ptr]
        parent_ptr = ptr



for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if len(min_heap)>1:
            delete()
        else:
            print(0)
    else:
        insert(tmp)