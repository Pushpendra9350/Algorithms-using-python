l=[-1,2,3,-6,5,9,-10,2,5,6,-3,-6,2]
# this is a BRUTE FORCE solution
# time complexity of this solution is O(n^2)
length=len(l)
maximum=-9999
for i in range(1,length):
    for j in range(length-i+1):
        # here we check all possible sub array and check maximum sum from them
        s=sum(l[j:j+i])
        if s>maximum:
            maximum=s
print(maximum)

# maximum subarray is [5,9,-10,2,5,6]

# this is KANANE'S solution
# time complexity of this solution is O(n)
local_max=0
for i in range(length):
    # this is the main logic of Kadane’s Algorithm this is an dynamic programming approach
    local_max=max(l[i],l[i]+local_max)
    # now check weather local_max is large or not
    if maximum<local_max:
        maximum=local_max
print(maximum)


#OUTPUT:
#17
