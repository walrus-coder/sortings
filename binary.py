# Бинарный поиск в отсортированном массиве за логарифмическое время
def binary(a,low,top,key):
    if top < low:
        return low
    mid = int((top + low) / 2)
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary(a, low, mid-1, key)
    else:
        return binary(a, mid+1, top, key)

# Если он не найдет нужного элемента, то вернет индекс, куда его нужно поставить, иначе вернет индекс самого элемента
if '__main__' == __name__:
    a = list(map(int, input().split()))
    key = int(input())
    ans = binary(a, 0, len(a)-1, key)
    print(ans)
