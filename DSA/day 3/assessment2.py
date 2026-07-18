arr = [1,2,3,4,5,6,7,8,9,10]
target = 7

start = 0
end = len(arr) - 1

while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
        print("Target found at index", mid)
        break
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
else:
    print("Target not found")

