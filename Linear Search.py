arr = [2,5,20,12,24]
target = 12

def linearSearch(arr,target):
    for i in range(len(arr)):
     if arr[i]==target:
        return i
    print("target not found")

result=linearSearch(arr,target)
print(result)

