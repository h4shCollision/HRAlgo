import unittest
from random import randint

def largestRectangle(x):
	if not x:
		return 0
	stack = []  # idx, value
	mx = 0
	for i in range(0, len(x)):
		if stack and x[i] > stack[-1][1]:
			stack.append((i, x[i]))
		else:
			idx = 0
			while len(stack) > 0 and stack[-1][1] > x[i]:
				idx, h = stack.pop()
				mx = max(mx, h * (i - idx))
			if len(stack) == 0 or stack[-1][1] < x[i]:
				stack.append((idx, x[i]))
	while len(stack) > 0:
		tmp = stack.pop()
		mx = max(mx, tmp[1] * (len(x) - tmp[0]))
	return mx


def largestRectangleInGrid(m):
	if not m or not m[0]:
		return 0
	dp = [0] * len(m[0])
	mx = 0
	for i in range(len(m)):
		for j in range(len(dp)):
			if m[i][j]:
				dp[j] = 0
			else:
				dp[j] += 1
		mx = max(mx, largestRectangle(dp))
	return mx

# test cases
class Test(unittest.TestCase):
	def test(self):
		for _ in range(10):
			x = [randint(0, 10) for _ in range(20)]
			size = largestRectangle(x)
			mx = 0
			for i in range(len(x)):
				for j in range(i + 1, len(x) + 1):
					mn = x[i]
					for k in range(i + 1, j):
						mn = min(mn, x[k])
					mx = max(mx, (j - i) * mn)
			self.assertEquals(size, mx)

	def testEdgeCases(self):
		self.assertEquals(largestRectangle([]), 0)
		self.assertEquals(largestRectangle([2]), 2)
		self.assertEquals(largestRectangle([1, 2, 3, 4, 5, 6]), 12)
		self.assertEquals(largestRectangle([6, 5, 4, 3, 2, 1]), 12)

	def testGrid(self):
		input = [[False, False, False, False, False, False, False, True, False],
				 [False, False, False, False, False, True, False, False, False],
				 [True, False, False, False, False, False, False, False, False],
				 [False, False, False, False, True, False, False, False, True],
				 [False, False, False, False, False, False, False, False, False],
				 [False, False, False, False, False, False, False, False, False],
				 [False, False, False, False, True, False, False, False, False],
				 [False, True, False, False, False, False, False, False, False],
				 [False, False, False, True, False, False, True, False, False]]
		self.assertEquals(largestRectangleInGrid(input), 21)
		self.assertEquals(largestRectangleInGrid([[False for _ in range(4)] for _ in range(4)]), 16)
		self.assertEquals(largestRectangleInGrid([[True for _ in range(4)] for _ in range(4)]), 0)

if __name__ == '__main__':
	unittest.main()
