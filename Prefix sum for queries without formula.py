arr = [2,3,4,5,6]
query = [[0,2],[1,3]]
def prefix_sum(arr,query):
    ans = []
    for q in query:
        l = q[0]
        r = q[1]
        sum =0
        for i in range(l,r+1):
            sum += arr[i]
        ans.append(sum)
    return ans
print(prefix_sum(arr,query))