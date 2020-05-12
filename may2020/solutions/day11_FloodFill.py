# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.

def floodFill(image, sr, sc, newColor):
    rows = len(image)
    cols = len(image[0])
    color = image[sr][sc]
    def dfs(r, c):
        if r<0 or r>=rows or c<0 or c>=cols:
            return
        if image[r][c] == color:
            image[r][c] = newColor
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
    if color != newColor:
        dfs(sr, sc)
    return image

# Alternate Solution:
# def floodFill(image, sr, sc, newColor):
#     rows = len(image)
#     cols = len(image[0])
#     color = image[sr][sc]
#     if color == newColor:
#         return image
#     def dfs(r, c):
#         if image[r][c] == color:
#             image[r][c] = newColor
#             if r>=1:
#                 dfs(r-1, c)
#             if r+1<rows:
#                 dfs(r+1, c)
#             if c>=1:
#                 dfs(r, c-1)
#             if c+1<cols:
#                 dfs(r, c+1)
#     dfs(sr, sc)
#     return image
