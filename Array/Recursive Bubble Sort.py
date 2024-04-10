def bubbleSort(arr: List[int], n: int):

    def rec_buble_sort(arr, n):
        if n == 1:
            return 
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        rec_buble_sort(arr, n - 1)

    return rec_buble_sort(arr, n)
