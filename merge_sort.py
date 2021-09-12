import math

# Рекурсивный алгоритм сортировки слиянием
def merge_sort(a,n):
    if n == 1:
        return a, 0
    a_1, inv1 = merge_sort(a[:int(n/2)], int(n/2))
    a_2, inv2 = merge_sort(a[int(n/2):], math.ceil(n/2))
    c, inv3 = merge(a_1, a_2, int(n/2), math.ceil(n/2))
    inv = inv1 + inv2 + inv3
    return c, inv

# Слияние двух отсортированных массивов a и b
def merge(a, b, n_a, n_b):
    sort_list = []
    i = 0
    j = 0
    inversions = 0
    while (i != n_a)&(j != n_b):
        if a[i] <= b[j]:
            sort_list.append(a[i])
            i += 1
        else:
            sort_list.append(b[j])
            j += 1
            inversions += n_a - i
    if i != n_a:
        sort_list = sort_list + a[i:]
    if j != n_b:
        sort_list = sort_list + b[j:]
    return sort_list, inversions
# Также выводит, сколько инверсий элементов массива было сделано при сортировке

if '__main__' == __name__:
    n = int(input())
    a = list(map(int, input().split()))
    ans, inv = merge_sort(a, n)
    #for i in ans:
    #    print(i, end = ' ')
    print(inv)
