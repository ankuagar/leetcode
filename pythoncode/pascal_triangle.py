#!/usr/bin/env python3
import unittest
cache = {}
def getElement(row, col):
    '''
    Get element in row'th row and col'th column of Pascal's triangle.

    row and col are row and column numbers respectively. row and col are 0 indexed
    row n has n+1 columns, e.g.
    row0 has 1 column: col0
    row1 has 2 columns: col0, col1
    row2 has 3 columns: col0, col1, col2

    item[row][col] = 1, if col = 0 or col == row
    item[row][col] = item[row-1][col-1] + item[row-1][col]
    '''
    if row < 0 or col < 0:
        return None
    elif col > row:
        return None
    elif col == 0 or col == row:
        '''
        setdefault(key[, default])
        If key is in the dictionary, return its value. 
        If not, insert key with a value of default and return default. 
        default defaults to None.
        '''
        return cache.setdefault((row, col), 1)
    else:
        return cache.setdefault((row, col), getElement(row-1, col-1) + getElement(row-1, col))

t = unittest.TestCase()
# row 0
t.assertEqual(1, getElement(0,0))
#print(cache)
# row 1
t.assertEqual(1, getElement(1,0))
t.assertEqual(1, getElement(1,1))
#print(cache)
# row 2
t.assertEqual(1, getElement(2,0))
t.assertEqual(2, getElement(2,1))
t.assertEqual(1, getElement(2,2))
#print(cache)
# row 3
t.assertEqual(1, getElement(3,0))
t.assertEqual(3, getElement(3,1))
t.assertEqual(3, getElement(3,2))
t.assertEqual(1, getElement(3,3))
#print(cache)
# row 4
t.assertEqual(1, getElement(4,0))
t.assertEqual(4, getElement(4,1))
t.assertEqual(6, getElement(4,2))
t.assertEqual(4, getElement(4,3))
t.assertEqual(1, getElement(4,4))
#print(cache)



def getRow(row):
    '''
    Get row'th row of Pascal's triangle.

    row and col are 0 indexed

    row n has n+1 columns, e.g.
    row0 has 1 column: col0
    row1 has 2 columns: col0, col1
    row2 has 3 columns: col0, col1, col2

    item[row][col] = 1, if col = 0 or col == row
    item[row][col] = item[row-1][col-1] + item[row-1][col]
    '''
    if row == 0:
        return [1]
    elif row == 1:
        return [1,1]
    elif row > 1:
        previousRow = getRow(row - 1)
        ans = [1,1]
        ans[1:1] = (previousRow[i] + previousRow[i+1]  for i in range(len(previousRow)-1))
        return ans

t = unittest.TestCase()
t.assertEqual(getRow(0), [1])
t.assertEqual(getRow(1), [1,1])
t.assertEqual(getRow(2), [1,2,1])
t.assertEqual(getRow(3), [1,3,3,1])
t.assertEqual(getRow(4), [1,4,6,4,1])