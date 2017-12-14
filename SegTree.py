class SegTree(object):

	#start incl, end excl
	def __init__(self, lst, start=0, end=None):
		if end is None:
			end=len(lst)
		self.start = start
		self.end = end
		if start == end-1:
			self.value = lst[start]
			self.lch = None
			self.rch = None
			return
		else:
			mid = (start + end + 1) / 2
			self.lch = SegTree(lst, start, mid)
			self.rch = SegTree(lst, mid, end)
			self.value = self.operation(self.lch.value, self.rch.value)

	def modify(self, idx, new):
		if idx<self.start or idx>=self.end:
			return
		elif idx==self.start and idx+1==self.end:
			self.value = new
		else:
			self.rch.modify(idx, new)
			self.lch.modify(idx, new)
			self.value = self.operation(self.lch.value, self.rch.value)

	def query(self, start, end):
		if start<=self.start and end>=self.end:
			return self.value
		if end<=self.start and start>=self.end:
			return 0
		mid = self.lch.end
		s=0
		if start < mid:
			s+=self.lch.query(start, end)
		if end > mid:
			s+=self.rch.query(start, end)
		return s

	def operation(self, x, y):
		return x+y


# test case from hell
from random import randint
l=[]
for i in range(20):
	l.append(randint(-100, 100))
tree = SegTree(l)
for _ in range(30):
	j = randint(0, len(l)-1)
	k = randint(0, len(l)-1)
	if k<j:
		j,k=k,j
	exp = 0
	for m in range(j,k):
		exp += l[m]
	assert exp == tree.query(j,k)

	j = randint(0, len(l)-1)
	k = randint(-100, 100)
	l[j] = k
	tree.modify(j, k)

print "ok"