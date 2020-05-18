# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.

# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    slope = (y1-y0)/(x1-x0)
    for x, y in coordinates[2:]:
        if (y-y0)/(x-x0) != slope:
            return False
    return True
