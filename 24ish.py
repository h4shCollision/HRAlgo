# https://en.wikipedia.org/wiki/24_Game
# This algorithm is based on the 24 game stated above, the only difference is we are not allowed to switch positions
# of the number is this problem, where as in 24 it is allowed.

# Problem statement: Given a list of numbers l, and another number y, can we add arithmetic operators + - * / and
# brackets in between numbers of l to create a valid expression that evaluates to y
# (We are not allowed to put two numbers together to make a new number, eg 6 7 => 67)
# Note in this solution brackets are not optimized.


dp = {}


# generate list of all possible answers and the expression that creates those values
def g(exprs, values, low, high):  # returns value: expression
	if high - low == 1:
		return {values[low]: str(exprs[low])}
	elif (low, high) in dp:
		return dp[low, high]
	else:
		d = {}
		for i in range(low + 1, high):
			first = g(exprs, values, low, i)
			last = g(exprs, values, i, high)

			for a1, e1 in first.iteritems():
				for a2, e2 in last.iteritems():
					if a2 != 0:
						d[a1 / a2] = "(%s/%s)" % (e1, e2)
					d[a1 + a2] = "(%s+%s)" % (e1, e2)
					d[a1 - a2] = "(%s-%s)" % (e1, e2)
					d[a1 * a2] = "(%s*%s)" % (e1, e2)
		dp[(low, high)] = d
	return d


def f(l, ans):
	values = map(float, l) # use floating point for calculation, integer for display
	d = g(l, values, 0, len(values))
	return d[ans][1:-1]

