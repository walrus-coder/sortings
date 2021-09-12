import math
import random

# Рекурсивное нахождение двух ближайших точек в двумерном декартовом пространстве и расстояния между ними за время n*log(n)
def closest_points(points_x, n_x):
    d_1 = None
    d_2 = None
    if n_x > 1:
        d_1, points_y_1 = closest_points(points_x[:int(n_x/2)], int(n_x/2))
        d_2, points_y_2 = closest_points(points_x[int(n_x/2):], n_x-int(n_x/2))
    else:
        return None, points_x
    # Слияние множеств точек, отсортированнных по оси у в предыдущих итерациях рекурсии
    points_y = merge(points_y_1, points_y_2, int(n_x/2), n_x-int(n_x/2))
    # Нахождение минимального расстояния из подмножеств точек, возвращенных из предыдущей итерации
    d = my_min(d_1, d_2)
    if d == None:
        return fun(points_x[0], points_x[1]), points_y
    median = (points_x[int(n_x/2)][0] + points_x[int(n_x/2) - 1][0]) / 2
    strip = []
    l = 0
    # Попытка найти расстояние меньшее d в полосе ширины d от линии слияния двух множеств
    for num in points_y:
        if (num[0] >= median - d)&(num[0] <= median + d):
            strip.append(num)
            l += 1
            for j in range(7):
                if 1+j < l:
                    ro = fun(strip[l-1], strip[l-1-j-1])
                    if ro < d:
                        d = ro
    return d, points_y

# Слияние отсортированных множесттв
def merge(a, b, n_a, n_b):
    sort_list = []
    i = 0
    j = 0
    while (i != n_a)&(j != n_b):
        if a[i][1] <= b[j][1]:
            sort_list.append(a[i])
            i += 1
        else:
            sort_list.append(b[j])
            j += 1
    if i != n_a:
        sort_list = sort_list + a[i:]
    if j != n_b:
        sort_list = sort_list + b[j:]
    return sort_list


def my_min(d_1, d_2):
    if d_1 == None:
        return d_2
    if d_2 == None:
        return d_1
    return min(d_1, d_2)

def fun(p_1, p_2):
    return math.sqrt((p_2[1] - p_1[1])**2 + (p_2[0] - p_1[0])**2)

# Быстрая сортировка
def sorting(a, l, r, key):
    if l >= r:
        return a
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r, key)
    sorting(a, l, m1 - 1, key);
    sorting(a, m2 + 1, r, key);
    return a

def partition3(a, l, r, key):
    x = a[l][key]
    j = l
    m_1 = l
    for i in range(l + 1, r + 1):
        if a[i][key] <= x:
            j += 1
            m_1 += 1
            a[i], a[j] = a[j], a[i]
            a[j], a[m_1] = a[m_1], a[j]
            if a[m_1][key] == x:
                m_1 -= 1
    a[l], a[j] = a[j], a[l]
    m_1 += 1
    return (m_1, j)

if '__main__' == __name__:
    n = int(input()) # Количество точек
    points_x = [0]*n
    for i in range(n):
        num = list(map(int, input().split())) # Координаты каждой из точек через пробел
        points_x[i] = num
    points_x = sorting(points_x, 0, n-1, 0) # Сортировка точек по координате Х
    ans = closest_points(points_x, n)
    print(ans[0])

