# given a list of points, calculate the smallest area rectangle that can be created from the points
# assume all x,y coordinates are integers
# assume rectangles must have sides parallel or perpendicular to the x/y axes
# assume no 2 points overlap
# return -1 if no rectangle is possible
# O(n^2) time (unless I screwed up) assuming const time dictionary insert/lookup

from collections import defaultdict
import unittest


def smallestRectangle(pts):
	axisMap = defaultdict(list)
	for x, y in pts:  # assume O(1) insertion: O(n) to build map
		axisMap[y].append(x)
	recMap = {}
	mnArea = -1
	coords = None  # blx, bly, w, h
	for y, xs in axisMap.iteritems():
		for i in range(len(xs)):
			pt1 = xs[i]
			for j in range(i + 1, len(xs)):  # execute this loop at most O(n^2) times
				pt2 = xs[j]
				# (minx, dx)
				key = (min(pt1, pt2), abs(pt1 - pt2))
				if key not in recMap:
					recMap[key] = [y]
				else:
					ys = recMap[key]
					minh = abs(ys[0] - y)
					othery = ys[0]
					for k in range(1, len(ys)):  # another O(n) -> more analysis later
						h = abs(ys[k] - y)
						if h < minh:
							minh = h
							othery = ys[k]
					area = minh * key[1]
					if mnArea == -1 or area < mnArea:
						mnArea = area
						coords = (key[0], min(othery, y), key[1], minh)
					ys.append(y)
	return mnArea, coords

# Analysis: when we multiple out the big O notations, it becomes O(n^3), however, process executes the loop starting at
# line 32(hope this doesn't change) exactly once per possible rectangle, it means # of executions of the innermost loop
# is capped at O(n^2), so total runtime is O(n^2)

# test cases
class Test(unittest.TestCase):
	def test(self):
		pts = [(-1, -1), (1, -1), (-1, 1), (1, 1),
			   (2, 2), (2, 1), (1, 2), (-1, 2), (2, -1), (0, 2), (1, 3)]
		self.assertEquals(smallestRectangle(pts), (1, (1, 1, 1, 1)))

	def testNoRec(self):
		pts = [(-1, -1), (1, -1), (-1, 1), (2, 2), (-1, 2), (0, 2), (1, 3)]
		self.assertEquals(smallestRectangle(pts), (-1, None))


if __name__ == '__main__':
	unittest.main()
