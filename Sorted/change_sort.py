def change_sort(matrix : list) -> list:
    for i in range(len(matrix)-1):
        minimum = matrix[i]
        ind = i
        for j in range(i+1, len(matrix)):
            if matrix[j] < minimum:
                minimum = matrix[j]
                ind = j
        
        if ind != i:
            k = matrix[i]
            matrix[i] = minimum
            matrix[ind] = k
    return matrix

if __name__ == '__main__':
    matrix = [-1,-1,0]
    change_sort(matrix)
    print(matrix)