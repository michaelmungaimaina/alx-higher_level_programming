#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """

    f n <= 0:
        return []

    limit = n - 1
    triangle = [[1]]

    for i in range(limit):
        row = []
        row.append(1)

        if len(triangle[i]) > 1:
            prev_row_len = len(triangle[i]) - 1
            nxt = 1

            for j in range(prev_row_len):
                suma = triangle[i][j] + triangle[i][nxt]
                row.append(suma)
                nxt += 1

        row.append(1)
        triangle.append(row)

    return triangle
