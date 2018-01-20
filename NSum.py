import unittest


# TODO: add backtracking and return result
def sortedTwoSum(m, a, b):
	if not a or not b:
		return False
	n = len(a) - 1
	i = 0
	j = len(b) - 1
	while i <= n and j >= 0:
		s = a[i] + b[j]
		if s == m:
			return True
		if s < m:
			i += 1
			if i > n:
				return False
		else:
			j -= 1
			if j < 0:
				return False
	return False


def twoSum(m, a, b):
	if not a or not b:
		return False
	return sortedTwoSum(m, sorted(a), sorted(b))


def threeSum(m, a, b, c):
	if not a or not b or not c:
		return False
	b.sort()
	c.sort()
	for i in a:
		if sortedTwoSum(m - i, b, c):
			return True
	return False


def fourSum(m, a, b, c, d):
	if not a or not b or not c or not d:
		return False

	def helper(x, y):
		n = len(x)
		l = [0] * (n * len(y))
		for c1, i in enumerate(x):
			for c2, j in enumerate(y):
				l[c1 * n + c2] = i + j
		return sorted(l)

	x = helper(a, b)
	y = helper(c, d)

	return sortedTwoSum(m, x, y)


# test cases
class Test(unittest.TestCase):
	# TODO: more tests
	def testEdge(self):
		self.assertTrue(twoSum(10, [0, 1, 1, 1, 1], [2, 2, 2, 2, 10]))
		self.assertTrue(twoSum(10, [0, 1, 1, 1, 1], [2, 2, 2, 2, 9]))
		self.assertTrue(threeSum(121, [1, 2], [10, 20], [100, 200]))
		self.assertTrue(fourSum(1212, [1, 2], [10, 20], [100, 200], [1000, 2000]))

	def testTwoSum(self):
		self.assertTrue(twoSum(10, [1, 2, 3, 5], [2, 6, 7, 10]))
		self.assertFalse(twoSum(14, [1, 2, 3, 5], [2, 6, 7, 10]))

	def testThreeSum(self):
		self.assertFalse(threeSum(10, [1, 2, 3, 5], [2, 6, 7, 10], [4, 10]))
		self.assertTrue(threeSum(17, [1, 2, 3, 5], [2, 6, 7, 10], [3, 7]))

	def testFourSum(self):
		self.assertFalse(fourSum(321, [1, 2], [10, 20], [100, 200], [1000, 2000]))


if __name__ == '__main__':
	unittest.main()
