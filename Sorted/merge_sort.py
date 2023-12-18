
def merge_list(a : list, b: list):
    c = []
    length_a = len(a)
    length_b = len(b)

    i, j = 0, 0

    while i < length_a and j < length_b:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    c += a[i:] + b[j:]
    return c


def split_merge_matrix(matrix : list):
    length_half = len(matrix) // 2
    N1 = matrix[:length_half]
    N2 = matrix[length_half:]

    if len(N1) > 1:
        N1 = split_merge_matrix(N1)

    if len(N2) > 1:
        N2 = split_merge_matrix(N2)

    return merge_list(N1, N2)

if __name__ == '__main__':
    matrix = [0, -1]
    print(split_merge_matrix(matrix))
    