#!/usr/bin/env python3
from operator import itemgetter
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
middle_start = len(matrix[0]) // 2 - 1
middle_end = middle_start + 2
the_middle = list(map(itemgetter(slice(middle_start, middle_end)), matrix))
print("The middle columns of the matrix are: {}".format(the_middle))