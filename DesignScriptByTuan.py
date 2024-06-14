# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#input data
numPointsX = int(IN[0])
distancePointsX = IN[1]
distanceY = IN[2]

#create list points at X1
points1 = []
for i in range(numPointsX):
    x = 0 + i * distancePointsX
    point = Point.ByCoordinates(x, 0, 4)
    points1.append(point)

#create list points at X2
points2 = []
for i in range(numPointsX):
    x = 0 + i * distancePointsX
    point = Point.ByCoordinates(x, distanceY/2, 4)
    points2.append(point)
    
#create list points at X3
points3 = []
for i in range(numPointsX):
    x = 0 + i * distancePointsX
    point = Point.ByCoordinates(x, distanceY, 4)
    points3.append(point)

#create X-shaped line
line12 = []
line21 = []
line23 = []
line32 = []
for i in range((numPointsX)-1):
    line12.append(Line.ByStartPointEndPoint(points1[i], points2[i+1]))
    line21.append(Line.ByStartPointEndPoint(points2[i], points1[i+1]))
    line23.append(Line.ByStartPointEndPoint(points2[i], points3[i+1]))
    line32.append(Line.ByStartPointEndPoint(points3[i], points2[i+1]))

#get key points    
pointA = Point.ByCoordinates(0, 0, 4)
pointA0 = Point.ByCoordinates(0, 0, 0)
pointB = Point.ByCoordinates((numPointsX-1) * distancePointsX, 0, 4)
pointB0 = Point.ByCoordinates((numPointsX-1) * distancePointsX, 0, 0)
pointC = Point.ByCoordinates(0, distanceY, 4)
pointC0 = Point.ByCoordinates(0, distanceY, 0)
pointD = Point.ByCoordinates((numPointsX-1) * distancePointsX, distanceY, 4)
pointD0 = Point.ByCoordinates((numPointsX-1) * distancePointsX, distanceY, 0)

#create vertical lines
lineA = Line.ByStartPointEndPoint(pointA, pointA0)
lineB = Line.ByStartPointEndPoint(pointB, pointB0)
lineC = Line.ByStartPointEndPoint(pointC, pointC0)
lineD = Line.ByStartPointEndPoint(pointD, pointD0)

#out put
OUT = pointA, pointB, pointC, pointD, pointA0, pointB0, pointC0, pointD0, line12, line21, line23, line32,lineA, lineB, lineC, lineD
    