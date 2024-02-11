def print_pascal(n):
    triangle = []
    for i in range(1, n + 1):
        rCe = 1
        temp = []
        for j in range(1, i + 1):
            temp.append(rCe)
            rCe = rCe * (i - j) // j  # Use // for integer division in Python 3
        triangle.append(temp)
    return triangle