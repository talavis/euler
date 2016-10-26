#!/usr/bin/env python3

import requests


def column(matrix, j):
    return [row[j] for row in matrix]


def find_pot(matrix, i, j):
    pot = [True]*10
    pot[0] = False
    curr = (square(matrix, i, j) + 
            row(matrix, i) +
            column(matrix, j))
    for c in set(curr):
        pot[c] = False
    if matrix[i][j] > 0:
        pot[matrix[i][j]] = True
    answer = [p[0] for p in enumerate(pot) if p[1] is True]
    return answer


def test_find_pot():
    matrix = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
              [9, 0, 0, 3, 0, 5, 0, 0, 1],
              [0, 0, 1, 8, 0, 6, 4, 0, 0],
              [0, 0, 8, 1, 0, 2, 9, 0, 0],
              [7, 0, 0, 0, 0, 0, 0, 0, 8],
              [0, 0, 6, 7, 0, 8, 2, 0, 0],
              [0, 0, 2, 6, 0, 9, 5, 0, 0],
              [8, 0, 0, 2, 0, 3, 0, 0, 9],
              [0, 0, 5, 0, 1, 0, 3, 0, 0]]
    expected = [4,5]
    assert find_pot(matrix, 0, 0) == expected
    expected = [4, 7, 8]
    assert find_pot(matrix, 6, 4) == expected


def get_data():
    import requests

    url = 'https://projecteuler.net/project/resources/p096_sudoku.txt'
    req = requests.get(url)
    return req.text


def brute(matrix):
    solution = [[c for c in line] for line in matrix]
    test = init_test_matrix(matrix)
    i_test = 0
    limit = 81
    while i_test < limit:
        fail = False
        i = i_test // 9
        j = i_test % 9
        if test[i][j]:
            pot = find_pot(solution, i, j)
            if solution[i][j] > 0:
                try:
                    solution[i][j] = pot[pot.index(solution[i][j])+1]
                except IndexError:
                    fail = True
            else:
                try:
                    solution[i][j] = pot[0]
                except IndexError:
                    fail = True
        if fail:
            solution[i][j] = 0
            i_test -= 1
            i = i_test // 9
            j = i_test % 9
            while not test[i][j]:
                i_test -= 1
                i = i_test // 9
                j = i_test % 9
        else:
            i_test += 1
#        print(i_test)
#        print(solution)
    return solution


def test_brute():
    sudoku = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
              [9, 0, 0, 3, 0, 5, 0, 0, 1],
              [0, 0, 1, 8, 0, 6, 4, 0, 0],
              [0, 0, 8, 1, 0, 2, 9, 0, 0],
              [7, 0, 0, 0, 0, 0, 0, 0, 8],
              [0, 0, 6, 7, 0, 8, 2, 0, 0],
              [0, 0, 2, 6, 0, 9, 5, 0, 0],
              [8, 0, 0, 2, 0, 3, 0, 0, 9],
              [0, 0, 5, 0, 1, 0, 3, 0, 0]]

    expected = [[4, 8, 3, 9, 2, 1, 6, 5, 7],
                [9, 6, 7, 3, 4, 5, 8, 2, 1],
                [2, 5, 1, 8, 7, 6, 4, 9, 3],
                [5, 4, 8, 1, 3, 2, 9, 7, 6],
                [7, 2, 9, 5, 6, 4, 1, 3, 8],
                [1, 3, 6, 7, 9, 8, 2, 4, 5],
                [3, 7, 2, 6, 8, 9, 5, 1, 4],
                [8, 1, 4, 2, 5, 3, 7, 6, 9],
                [6, 9, 5, 4, 1, 7, 3, 8, 2]]

    assert brute(sudoku) == expected
    

def init_test_matrix(matrix):
    test = [[True for i in range(len(matrix))] for i in range(len(matrix[0]))]
            
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                test[i][j] = False
    return test


def test_init_test_matrix():
    sudoku = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
              [9, 0, 0, 3, 0, 5, 0, 0, 1],
              [0, 0, 1, 8, 0, 6, 4, 0, 0],
              [0, 0, 8, 1, 0, 2, 9, 0, 0],
              [7, 0, 0, 0, 0, 0, 0, 0, 8],
              [0, 0, 6, 7, 0, 8, 2, 0, 0],
              [0, 0, 2, 6, 0, 9, 5, 0, 0],
              [8, 0, 0, 2, 0, 3, 0, 0, 9],
              [0, 0, 5, 0, 1, 0, 3, 0, 0]]

    expected = [[True, True, False, True, False, True, False, True, True],
                [False, True, True, False, True, False, True, True, False],
                [True, True, False, False, True, False, False, True, True],
                [True, True, False, False, True, False, False, True, True],
                [False, True, True, True, True, True, True, True, False],
                [True, True, False, False, True, False, False, True, True],
                [True, True, False, False, True, False, False, True, True],
                [False, True, True, False, True, False, True, True, False],
                [True, True, False, True, False, True, False, True, True]]

    assert init_test_matrix(sudoku) == expected


def main():
    raw = get_data()
    matrices = parse_data(raw)
    upper_sum = 0
    for mat in matrices:
        sol = brute(mat)
        upper_sum += (sol[0][0] * 100 +
                      sol[0][1] * 10 +
                      sol[0][2])
    print(upper_sum)


def parse_data(raw):
    matrices = list()
    lines = raw.split('\n')
    matrix = list()
    for i in range(len(lines)):
        if i % 10 == 0:
            if len(matrix) > 0:
                matrices.append(matrix)
            matrix = list()
            continue
        matrix.append([int(c) for c in lines[i]])
    if len(matrix) > 0:
        matrices.append(matrix)
    return matrices


def test_parse_data():
    indata = ('Grid 02\n' +
              '200080300\n' +
              '060070084\n' +
              '030500209\n' +
              '000105408\n' +
              '000000000\n' +
              '402706000\n' +
              '301007040\n' +
              '720040060\n' +
              '004010003\n') * 2

    expected = [[[2, 0, 0, 0, 8, 0, 3, 0, 0],
                 [0, 6, 0, 0, 7, 0, 0, 8, 4],
                 [0, 3, 0, 5, 0, 0, 2, 0, 9],
                 [0, 0, 0, 1, 0, 5, 4, 0, 8],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [4, 0, 2, 7, 0, 6, 0, 0, 0],
                 [3, 0, 1, 0, 0, 7, 0, 4, 0],
                 [7, 2, 0, 0, 4, 0, 0, 6, 0],
                 [0, 0, 4, 0, 1, 0, 0, 0, 3]],
                [[2, 0, 0, 0, 8, 0, 3, 0, 0],
                 [0, 6, 0, 0, 7, 0, 0, 8, 4],
                 [0, 3, 0, 5, 0, 0, 2, 0, 9],
                 [0, 0, 0, 1, 0, 5, 4, 0, 8],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [4, 0, 2, 7, 0, 6, 0, 0, 0],
                 [3, 0, 1, 0, 0, 7, 0, 4, 0],
                 [7, 2, 0, 0, 4, 0, 0, 6, 0],
                 [0, 0, 4, 0, 1, 0, 0, 0, 3]]]
                
    assert parse_data(indata) == expected


def prep_print_matrix(matrix):
    out = ''
    for i in range(len(matrix)):
        out += str(matrix[i]) + '\n'
    return out


def row(matrix, i):
    return matrix[i]

    
def square(matrix, i, j):
    if i < 3:
        i_c = (0,3)
    elif i < 6:
        i_c = (3,6)
    else:
        i_c = (6,9)
    if j < 3:
        j_c = (0,3)
    elif j < 6:
        j_c = (3,6)
    else:
        j_c = (6,9)
    tmp = [cols[j_c[0]:j_c[1]] for cols in matrix[i_c[0]:i_c[1]]]
    return tmp[0] + tmp[1] + tmp[2]


def test_square():
    matrix = [[4, 8, 3, 9, 2, 1, 6, 5, 7],
              [9, 6, 7, 3, 4, 5, 8, 2, 1],
              [2, 5, 1, 8, 7, 6, 4, 9, 3],
              [5, 4, 8, 1, 3, 2, 9, 7, 6],
              [7, 2, 9, 5, 6, 4, 1, 3, 8],
              [1, 3, 6, 7, 9, 8, 2, 4, 5],
              [5, 7, 2, 6, 8, 9, 5, 1, 4],
              [8, 1, 4, 2, 5, 3, 7, 6, 9],
              [6, 9, 5, 4, 1, 7, 3, 8, 2]]
    expected = (matrix[0][0:3] +
                matrix[1][0:3] +
                matrix[2][0:3])
    assert square(matrix, 1, 1) == expected
    expected = (matrix[3][6:9] +
                matrix[4][6:9] +
                matrix[5][6:9])
    assert square(matrix, 5, 8) == expected
    expected = (matrix[6][3:6] +
                matrix[7][3:6] +
                matrix[8][3:6])
    assert square(matrix, 6, 3) == expected


if __name__ == '__main__':
    main()
    
