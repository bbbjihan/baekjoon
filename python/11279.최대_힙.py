import sys

N = int(sys.stdin.readline())
heap = [2**31]

def insert(num,heap):
    heap.append(num)
    idx = len(heap)-1
    if idx > 1:
        parent = idx//2
        while idx != 1 and heap[parent]<=heap[idx]:
            heap[parent],heap[idx] = heap[idx],heap[parent]
            idx = parent
            parent = idx//2
            
def delete(heap):
    idx = len(heap)-1
    if idx == 1:
        print(heap.pop())
    else:
        heap[1],heap[idx] = heap[idx],heap[1]
        print(heap.pop())
        parent = 1
        child = 2
        while 1:
            if child+1<len(heap):
                if heap[child]<heap[child+1]:
                    child+=1
            if child<len(heap):
                if heap[parent]<heap[child]:
                    heap[parent],heap[child] = heap[child],heap[parent]
                    parent = child
                    child = parent*2
                else:
                    break
            else:
                break

for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if len(heap)>1:
            delete(heap)
        else:
            print(0)
    else:
        insert(tmp,heap)