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

# 示例用法
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", nums)
    bubble_sort(nums)
    print("排序后:", nums)