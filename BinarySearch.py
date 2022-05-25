def binary_search(arr,x):
    left=0
    right=len(arr)-1
    while left <= right:
        mid=left+(right-left)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid+1
        elif arr[mid] > x:
            right = mid-1

    return -1

arr=[1,2,3,4,5,6]
result=binary_search(arr,9)
if result==-1:
    print("element not found")
else:
    print("element found at",result)