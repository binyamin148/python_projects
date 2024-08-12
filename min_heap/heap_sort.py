from min_heap import MinHeap

def heap_sort(arr):
    if not arr:
        return []
    
    heap = MinHeap()
    
    for item in arr:
        heap.insert(item)
    
    sorted_arr = []
    while not heap.is_empty():
        min_val = heap.extract_min()
        if min_val is not None:
            sorted_arr.append(min_val)
    
    return sorted_arr