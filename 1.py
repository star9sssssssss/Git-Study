def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 提前退出标志
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 实现快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 先使用冒泡排序
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", nums)
    bubble_sort(nums)
    print("排序后:", nums)
    # 使用之前的快速排序
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("快速排序前:", nums)
    sorted_nums = quick_sort(nums)
    print("快速排序后:", sorted_nums)
