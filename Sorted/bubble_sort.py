def bubble_sort(matrix : list) -> list:
    for i in range(len(matrix)-1):
        for j in range(len(matrix)-1):
            if matrix[j] > matrix[j+1]:
                matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
   



if __name__ == '__main__':
    matrix = [10, -1, 0 ,6, 9, 4, 2, -8]
    
