import sys

N = int(sys.stdin.readline())
heap = [None]

def insert(num):
    heap.append(num)
    ptr = len(heap)-1
    parent = ptr//2
    while 1:
        if ptr == 1:
            break
        elif abs(heap[parent]) == abs(heap[ptr]) and heap[parent] <= heap[ptr]:
            break
        elif abs(heap[parent]) < abs(heap[ptr]):
            break
        elif (abs(heap[parent]) == abs(heap[ptr]) and heap[parent] > heap[ptr]) or (abs(heap[parent]) > abs(heap[ptr])):
            heap[parent], heap[ptr] = heap[ptr], heap[parent]
            ptr = parent
            parent = ptr//2

def delete():
    ptr = len(heap)-1
    if ptr == 0:
        return 0
    elif ptr == 1:
        return heap.pop()
    else:
        heap[1], heap[ptr] = heap[ptr], heap[1]
        poped = heap.pop()
        ptr = 1
        child = 2
        while 1:
            if child >= len(heap):
                break
            elif child != len(heap)-1:
                if abs(heap[child]) > abs(heap[child+1]) or (abs(heap[child]) == abs(heap[child+1]) and heap[child] > heap[child+1]):
                    child+=1
            if (abs(heap[ptr]) < abs(heap[child])) or (abs(heap[child]) == abs(heap[ptr]) and heap[ptr] <= heap[child]):
                break
            elif abs(heap[ptr]) >= abs(heap[child]) or (abs(heap[child]) == abs(heap[ptr]) and heap[ptr] > heap[child]):
                heap[ptr], heap[child] = heap[child], heap[ptr]
                ptr = child
                child = ptr * 2
    return poped

for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        print(delete())
    else:
        insert(tmp)