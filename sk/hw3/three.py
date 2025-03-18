import math

num = [18, 24]

avg = sum(num) / len(num)
avg_geometric = round(math.sqrt(sum(num)), 4)

print(avg)
print(avg_geometric)
