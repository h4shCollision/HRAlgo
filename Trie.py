charCount=26

class Trie(object):
	def __init__(self):
		self.count=0
		self.children=0
		self.lst=[None]*charCount

	def add(self, string, idx=0):
		self.children += 1
		if idx==len(string):
			self.count+=1
			return
		i=ord(string[idx])-ord('a')
		if not self.lst[i]:
			self.lst[i] = Trie()
		self.lst[i].add(string, idx+1)

	def queryCount(self, string, idx=0):
		if idx==len(string):
			return self.count
		i=ord(string[idx])-ord('a')
		if not self.lst[i]:
			return 0
		return self.lst[i].queryCount(string, idx+1)

	def queryChildren(self, string, idx=0):
		if idx==len(string):
			return self.children
		i=ord(string[idx])-ord('a')
		if not self.lst[i]:
			return 0
		return self.lst[i].queryChildren(string, idx+1)

	def exist(self, string):
		return self.query(self, string) > 0

#test cases
string = ["jkdhfaksjfk", "asfdjkasjfd", "askdjfha", "asdfwera"]
root=Trie()
for s in string:
	for i in range(len(s)):
		root.add(s[i:])

assert root.queryCount("jfk") == 1
assert root.queryCount("aks") == 0
assert root.queryCount("a") == 2
assert root.queryChildren("a") == 7
assert root.queryChildren("mn") == 0
assert root.queryChildren("jf") == 3

print "ok"