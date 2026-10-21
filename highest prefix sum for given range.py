arr = [6,4,8,2,9,5]
query = [[0,2],[1,4],[3,5]]
def prefix_sum(arr,query):
    for q in query:
        l = q[0]
        r = q[1]
        current_sum = 0
        maximum_sum  = float("-inf")
        for i in range(l,r+1):
            current_sum += arr[i]
            maximum_sum = max(maximum_sum,current_sum)
        print(maximum_sum)
print(prefix_sum(arr,query))