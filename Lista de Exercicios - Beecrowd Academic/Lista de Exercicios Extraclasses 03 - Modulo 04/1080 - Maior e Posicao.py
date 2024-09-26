highest_no = 0
pos_highest_no = 0

for pos in range(1, 101, 1):
    no = int(input())

    if no >= highest_no:
        highest_no = no
        pos_highest_no = pos

print(highest_no)
print(pos_highest_no)
