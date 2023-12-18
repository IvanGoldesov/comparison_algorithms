
def quick_sort(matrix : list):
    a1 = []
    a2 = []
    a3 = []

    length = len(matrix)

    if length > 1:
        num = matrix[length//2]
        for i in range(length):
            if matrix[i] < num:
                a1.append(matrix[i])
            elif matrix[i] == num:
                a2.append(matrix[i])
            else:
                a3.append(matrix[i])

        return (quick_sort(a1) + a2 + quick_sort(a3))
    else:
        return matrix
    

if __name__ == '__main__':
    matrix = [10, -1, 0 ,6, 9, 4, 2, -8]
    a = quick_sort(matrix)
    print(a)