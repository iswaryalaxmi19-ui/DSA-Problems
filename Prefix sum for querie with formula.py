arr = [3,4,5,6,7,8]
query = [[2,4],[0,5]]
def prefix_sum(arr,query):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    ans = []
    for q in query:
        l = q[0]
        r = q[1]
        if l == 0:
            sum = prefix[r]
        else :
            sum = prefix[r] - prefix[l-1]
        ans.append(sum)
    return ans
print(prefix_sum(arr,query))