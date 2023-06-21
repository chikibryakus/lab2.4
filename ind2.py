lst = [-3.5, 2.1, 4.7, -1.2, 0, -5.6, 3.8, 2.9, -2.3]

# максимальный по модулю элемент списка
max_abs = max(lst, key=abs)
print("Максимальный по модулю элемент списка:", max_abs)

# сумма элементов списка, расположенных между первым и вторым положительными элементами
sum_between = 0
positive_count = 0
for i in range(len(lst)):
    if lst[i] > 0:
        positive_count += 1
if positive_count == 1:
    start_index = i
elif positive_count == 2:
    end_index = i

if positive_count < 2:
    print("Недостаточно положительных элементов в списке")
else:
    sum_between = sum(lst[start_index+1:end_index])
print("Сумма элементов списка, расположенных между первым и вторым положительными элементами:", sum_between)
