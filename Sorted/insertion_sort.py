
def insertion_sort(matrix : list) -> list:
    for i in range(1, len(matrix)):
        for j in range(i, 0, -1):
            if matrix[j] < matrix[j-1]:
                matrix[j], matrix[j-1] = matrix[j-1], matrix[j]
    return matrix

if __name__ == '__main__':
    matrix = [10, -1, 0 ,6, 9, 4, 2, -8]
    insertion_sort(matrix)
    print(matrix)