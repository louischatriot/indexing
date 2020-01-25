from timing import time_execution









print("=================")

N = 1000000
res = 0


with time_execution("blah"):
    for i in range(0,N):
        res += i


print(res)

