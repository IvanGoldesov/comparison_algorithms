
def quick_sort_Hoara(matrix : list, start : int, ends : int) -> list:
    if start >= ends:
        return 
    
    i = start
    j = ends

    num = matrix[(i+j)//2]

    while i <= j:
        while matrix[i] < num: i += 1
        while matrix[j] > num: j -= 1
        if i <= j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
    
    quick_sort_Hoara(matrix, start, j)
    quick_sort_Hoara(matrix, i, ends)

    return matrix


if __name__ == '__main__':
    matrix = [10, -1, 0 ,6, 9, 4, 2, -8, 1000, 1254, -12093, 123, 1515, 123123]
    quick_sort_Hoara(matrix, 0, len(matrix)-1)