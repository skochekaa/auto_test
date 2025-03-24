def fibonachi():
    num_list = [0, 1]
    while True:
        sum_list = sum(num_list)
        yield sum_list
        num_list.pop(0)
        num_list.append(sum_list)


count = 1
num_print = (5, 200, 1000, 100000)
for num in fibonachi():
    if count in num_print:
        print(num)
    if count == max(num_print):
        break
    count += 1
