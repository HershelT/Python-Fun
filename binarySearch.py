def binarySearch(arr: list, start: int, end: int, num: int):
    mid = int((start + end) / 2)
    if start > end: return (f"Problem: {num} not in Array")
    elif arr[mid] == num: return (f'Index of {num} is ({mid})')
    elif arr[mid] < num: return binarySearch(arr, mid + 1, end, num)   
    elif arr[mid] > num: return binarySearch(arr, start, end-1, num)
a = [1, 3, 5, 7, 8, 9, 10, 13, 15, 16, 17, 19, 23, 26, 2, 6, 11, 38, 111, 0]   
a.sort()
print(a)
print(binarySearch(a, 0, len(a) - 1, 23))
