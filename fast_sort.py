# Uses python3
import sys
import random

#Становление элемента в правильное положение и всех элементов одинакого с ним значеения
def partition3(a, l, r):
    x = a[l]
    j = l
    m_1 = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            m_1 += 1
            a[i], a[j] = a[j], a[i]
            a[j], a[m_1] = a[m_1], a[j]
            if a[m_1] == x:
                m_1 -= 1
    a[l], a[j] = a[j], a[l]
    m_1 += 1
    return (m_1, j)

# Становление элемента в правильное положение без учета повторяющихся значений
def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

# Сама сортировка со случайным выбором опорного элемента
def randomized_quick_sort(a, l, r):
    if l >= r:
        return 
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
#    input = sys.stdin.read()
    n = int(input())
    a = list(map(int, input().split())) # Элементы массива вводятся в строке через пробел
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
