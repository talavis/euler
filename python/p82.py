#!/usr/bin/env python3
'''
Find the minimal path sum, in matrix.txt, a 31K text file
containing a 80 by 80 matrix, from the left column to the right column.
'''


def get_data():
    '''
    Download the matrix
    '''
    import requests
    url = 'https://projecteuler.net/project/resources/p082_matrix.txt'
    page_req = requests.get(url)
    return page_req.text


def parse_data(raw):
    '''
    Build the matrix from the read data
    '''
    lines = raw.split('\n')
    matrix = [l.split(',') for l in lines if len(l) > 0]
    matrix = [[int(i) for i in l] for l in matrix]
    return matrix


def find_path_sum(matrix):
    '''
    Find the optimal path from left to right column
    Diretions: up, down, right
    '''
    for x in range(1, len(matrix[0])):
        new = [0]*len(matrix)
        new[0] = matrix[0][x-1] + matrix[0][x]
        # check down
        for y in range(1, len(matrix)):
            right = matrix[y][x-1] + matrix[y][x]
            down = new[y-1] + matrix[y][x]
            new[y] = min(right, down)
        # check up
        for y in range(len(matrix)-2, -1, -1):
            new[y] = min(new[y], new[y+1] + matrix[y][x])
        for y in range(len(matrix)):
            matrix[y][x] = new[y]
    return min([l[-1] for l in matrix])


def test_find_path_sum():
    '''
    Test find_path()
    '''
    matrix = [[131, 673, 234, 103, 18],
              [201, 96, 342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]

    assert find_path_sum(matrix) == 994


if __name__ == '__main__':
    RAW = get_data()
    MATRIX = parse_data(RAW)
    print(find_path_sum(MATRIX))
