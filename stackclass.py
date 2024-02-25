class Stack(object):
	
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

s = Stack()
print (s.isEmpty()) 	# true
s.push('two')
print(s.peek())
s.push(True)
print(s.size()) 			# 1
print(s.isEmpty()) 		# false
print(s.pop()) 			# 'two