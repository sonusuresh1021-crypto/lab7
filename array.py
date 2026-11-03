import sys
scores = list(map(int,sys.argv[1:]))
total = sum(scores)
Average=total/len(scores)


print("total:",total)
print("Average:",average)

maximum = max(scores)
minimum = min(scores)

print("maximum",maximum)
print("minimum",minimum)
