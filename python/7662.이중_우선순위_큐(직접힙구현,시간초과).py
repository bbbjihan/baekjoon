import sys
from collections import deque

T = int(sys.stdin.readline())

def insert(num,min_heap,max_heap):
    min_heap.append(num)
    max_heap.append(num)
    #최소힙에서 삽입
    min_idx = len(min_heap)-1
    min_parent = min_idx//2
    while min_idx > 1 and min_heap[min_parent][0] > min_heap[min_idx][0]:
        min_heap[min_parent],min_heap[min_idx] = min_heap[min_idx],min_heap[min_parent]
        min_idx = min_parent
        min_parent = min_idx//2
    #최대힙에서 삽입
    max_idx = len(max_heap)-1
    max_parent = max_idx//2
    while max_idx > 1 and max_heap[max_parent][0] < max_heap[max_idx][0]:
        max_heap[max_parent],max_heap[max_idx] = max_heap[max_idx],max_heap[max_parent]
        max_idx = max_parent
        max_parent = max_idx//2

def del_root_inminheap(heap,deleted):
    heap[1],heap[len(heap)-1] = heap[len(heap)-1], heap[1]
    deleted[heap.pop()[1]] = True
    idx = 1
    child = idx * 2
    while child < len(heap):
        if child+1 < len(heap) and heap[child][0] > heap[child+1][0]:
            child+=1
        if heap[idx][0] > heap[child][0]:
            heap[idx],heap[child] = heap[child],heap[idx]
            idx = child
            child = idx * 2

def del_root_inmaxheap(heap,deleted):
    heap[1],heap[len(heap)-1] = heap[len(heap)-1], heap[1]
    deleted[heap.pop()[1]] = True
    idx = 1
    child = idx * 2
    while child < len(heap):
        if child+1 < len(heap) and heap[child][0] < heap[child+1][0]:
            child+=1
        if heap[idx][0] < heap[child][0]:
            heap[idx],heap[child] = heap[child],heap[idx]
            idx = child
            child = idx * 2


def delete(num,min_heap,max_heap,deleted):
    if not any(min_heap) or not any(max_heap):
        return
    if num == 1:
        while deleted[max_heap[1][1]]==True:
           del_root_inmaxheap(max_heap,deleted)
        del_root_inmaxheap(max_heap,deleted)
    else:
        while deleted[min_heap[1][1]]==True:
            del_root_inminheap(min_heap,deleted)
        del_root_inminheap(min_heap,deleted)

for _ in range(T):
    N = int(sys.stdin.readline())
    min_heap = [None]
    max_heap = [None]
    deleted = [False for _ in range(N+1)]
    for i in range(N):
        command = sys.stdin.readline().rstrip().split()
        if command[0] == 'I':
            insert((int(command[1]),i),min_heap,max_heap)
        else:
            delete(int(command[1]),min_heap,max_heap,deleted)
    
    if not any(min_heap) or not any(max_heap):
        print('EMPTY')
    else:
        while deleted[max_heap[1][1]]==True:
           del_root_inmaxheap(max_heap,deleted)
        while deleted[min_heap[1][1]]==True:
            del_root_inminheap(min_heap,deleted)
        print(max_heap[1][0],min_heap[1][0])