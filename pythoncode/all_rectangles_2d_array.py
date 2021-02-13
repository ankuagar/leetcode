#!/usr/bin/env python3

"""
Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0.

The image you get is known to have potentially many distinct rectangles of 0s on a background of 1's. Write a function that takes in the image and returns the coordinates of all the 0 rectangles -- top-left and bottom-right; or top-left, width and height.

image1 = [
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]

Sample output variations (only one is necessary):

findRectangles(image1) =>
  // (using top-left-row-column and bottom-right):
  [
    [[0,0],[0,0]],
    [[2,0],[2,0]],
    [[2,3],[3,5]],
    [[3,1],[5,1]],
    [[5,3],[6,4]],
    [[7,6],[7,6]],
  ]
  // (using top-left-row-column and width/height):
  [
    [[0,0],[1,1]],
    [[2,0],[1,1]],
    [[2,3],[3,2]],
    [[3,1],[1,3]],
    [[5,3],[2,2]],
    [[7,6],[1,1]],
  ]

Other test cases:

image2 = [
  [0],
]

findRectangles(image2) =>
  // (using top-left-row-column and bottom-right):
  [
    [[0,0],[0,0]],
  ]

  // (using top-left-row-column and width/height):
  [
    [[0,0],[1,1]],
  ]

image3 = [
  [1],
]

findRectangles(image3) => []

image4 = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1],
]

findRectangles(image4) =>
  // (using top-left-row-column, and bottom-right or width/height):
  [
    [[1,1],[3,3]],
  ]

n: number of rows in the input image
m: number of columns in the input image


"""

image1 = [
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]

image2 = [
  [0],
]

image3 = [
  [1],
]

image4 = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1],
]
import unittest
import copy
def findRectangle(image):
    """
    Assumptions:
    1. There is 0 or 1 rectangle only
    """
    imageCopy = copy.deepcopy(image)
    topLeft, width, height = [], -1, -1
    for rowNum, row in enumerate(imageCopy):
        if all(row):
            continue
        else:
            if len(topLeft) == 0:
                width, height = row.count(0), 1
                topLeft = [rowNum, row.index(0)]
            else:
                height += 1
    if len(topLeft) == 0:
        return topLeft
    else:
        return [[topLeft, [width, height]]]

t = unittest.TestCase()
t.assertEqual([[[0, 0], [1, 1]]], findRectangle(image2))
t.assertEqual([], findRectangle(image3))
t.assertEqual([[[1, 1], [3, 3]]], findRectangle(image4))


def findRectangles(image):
    """
    Assumptions:
    1. There are multiple rectangles 
    2. Rectangles do not overlap
    """
    imageCopy = copy.deepcopy(image)
    ans = []
    for rownum, row in enumerate(imageCopy):
        while not all(row):
#             print(f"""[
#   [0, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1],
#   [0, 1, 1, 0, 0, 0, 1],
#   [1, 0, 1, 0, 0, 0, 1],
#   [1, 0, 1, 1, 1, 1, 1],
#   [1, 0, 1, 0, 0, 1, 1],
#   [1, 1, 1, 0, 0, 1, 1],
#   [1, 1, 1, 1, 1, 1, 0],
# ]""")
            # print(f"rownum = {rownum}, row = {row}")
            colnum0 = row.index(0) #get col number that has a 0
            topLeft = [rownum, colnum0] # store top left coordinates for the rectangle
            width, height = 0, 1
            while colnum0 < len(row) and row[colnum0] == 0: # compute width of this rectangle
                width += 1
                colnum0 += 1
            # print(f"colnum0 - width = {colnum0 - width}, width = {width}")
            row[colnum0-width:colnum0] = [1] * width # slice assignment of all 0s to 1s in current row
            # print(f"After assignment of 1s: rownum = {rownum}, row = {row}")
            rownum0 = rownum + 1 # row number of next row
            # print(rownum0, colnum0 - width, width)
            while rownum0 < len(imageCopy) and imageCopy[rownum0][colnum0 - width] == 0:
                height += 1
                imageCopy[rownum0][colnum0 - width:colnum0] = [1] * width # slice assignment of all 0s to 1s in row below which are part of current rectangle
                rownum0 += 1
            ans.append([topLeft, [width, height]])
            # print("--")
    return ans

t = unittest.TestCase()
t.assertEqual([
    [[0,0],[1,1]],
    [[2,0],[1,1]],
    [[2,3],[3,2]],
    [[3,1],[1,3]],
    [[5,3],[2,2]],
    [[7,6],[1,1]],
  ], findRectangles(image1))

t.assertEqual([
    [[0,0],[1,1]],
  ], findRectangles(image2))

t.assertEqual([], findRectangles(image3))

t.assertEqual(  [
    [[1,1],[3,3]],
  ], findRectangles(image4))