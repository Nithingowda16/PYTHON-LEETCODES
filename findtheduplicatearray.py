def find_duplicate(arr):
    # Initialize tortoise and hare pointers.
    tortoise = arr[0]
    hare = arr[0]

    # Find the intersection point of the two runners.
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]

    # Find the entrance to the cycle.
    tortoise = arr[0]
    while tortoise != hare:
        # Both runners move with the same speed.
        tortoise = arr[tortoise]
        hare = arr[hare]

    # Return the entrance to the cycle, which is the repeated element.
    return hare

