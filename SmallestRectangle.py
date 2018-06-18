# given a list of points, calculate the smallest area rectangle that can be created from the points
# assume all x,y coordinates are integers
# assume rectangles must have sides parallel or perpendicular to the x/y axes
# assume no 2 points overlap
# return -1 if no rectangle is possible
# O(n^2) time (unless I screwed up) assuming const time dictionary insert/lookup
# coordinates from lower left corner to upper right corner (x1, y1, x2, y2)

from collections import defaultdict
import unittest


def smallestRectangle(pts):
	axisMap = defaultdict(list)
	for x, y in pts:  # assume O(1) insertion: O(n) to build map
		axisMap[y].append(x)
	recMap = {}
	mnArea = -1
	coords = None  # blx, bly, w, h
	for y, xs in sorted(axisMap.iteritems()): # O(n log n) to sort
		for i in range(len(xs)):
			pt1 = xs[i]
			for j in range(i + 1, len(xs)):  # since (pt1, y), (pt2, y) are distinct pts of the input set, execute this
											# loop at most O(n^2) times
				pt2 = xs[j]
				# (minx, dx)
				key = (min(pt1, pt2), abs(pt1 - pt2))
				if key not in recMap:
					recMap[key] = y
				else:
					othery = recMap[key]
					area = (y - othery) * key[1]
					if mnArea == -1 or area < mnArea: # change this line if calculating largest rectangle
						mnArea = area
						coords = (key[0], othery, key[0] + key[1], y)
					recMap[key] = y # remove this line if calculating largest rectangle
	return mnArea, coords


# test cases
class Test(unittest.TestCase):
	def test(self):
		pts = [(-1, -1), (1, -1), (-1, 1), (1, 1),
			   (2, 2), (2, 1), (1, 2), (-1, 2), (2, -1), (0, 2), (1, 3)]
		self.assertEquals(smallestRectangle(pts), (1, (1, 1, 2, 2)))

	def testNoRec(self):
		pts = [(-1, -1), (1, -1), (-1, 1), (2, 2), (-1, 2), (0, 2), (1, 3)]
		self.assertEquals(smallestRectangle(pts), (-1, None))


if __name__ == '__main__':
	unittest.main()
