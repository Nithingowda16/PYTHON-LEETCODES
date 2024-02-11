def sort012(arr, n):
    i = 0
    next_zero = 0
    next_two = n - 1

    while i <= next_two:
        if arr[i] == 0:
            i += 1
            next_zero += 1
        elif arr[i] == 2:
            arr[i], arr[next_two] = arr[next_two], arr[i]
            next_two -= 1
        else:
            i += 1



