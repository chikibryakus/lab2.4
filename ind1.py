lst = [1, 0, 5, 0, 3, 0, 7]

count = 0
zero_indexes = []

for i in range(len(lst)):
                if lst[i] == 0:
                        count += 1
                zero_indexes.append(i)

print("Number of zeros:", count)
print("Indexes of zeros:", zero_indexes)