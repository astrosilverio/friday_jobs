from random import choice
from random import randint

# It will be useful to have stacks and queues later
# defining them first

class Stack(object):
	def __init__(self):
		self.stack = []
		
	def push(self, item):
		self.stack.append(item)
		
	def pop(self):
		return self.stack.pop()
		
	def peek(self):
		return self.stack[-1]
		
	def isEmpty(self):
		return self.stack == []
		
	def size(self):
		return len(self.stack)
		
class Queue(object):
	def __init__(self):
		self.items = Stack()
		self.backwards = Stack()
		
	def push(self, item):
		self.items.push(item)
	
	def pop(self):
		if self.items.isEmpty() and self.backwards.isEmpty():
			return None
		else:
			while not self.items.isEmpty():
				self.backwards.push(self.items.pop())
		
			popper = self.backwards.pop()
		
			while not self.backwards.isEmpty():
				self.items.push(self.backwards.pop())
				
			return popper
			
	def peek(self):
		if self.items.isEmpty() and self.backwards.isEmpty():
			return -1
		else:
			while not self.items.isEmpty():
				self.backwards.push(self.items.pop())
			
			peekee = self.backwards.peek()
		
			while not self.backwards.isEmpty():
				self.items.push(self.backwards.pop())
				
			return peekee
		
	def isEmpty(self):
		return self.items.stack == []
		
	def size(self):
		return self.items.size()
		
# Naive fibonacci
# (note: we can do fibonacci numbers in O(log n) using transformations a la SICP 1.19)

def fib(n):
	'''recursive fibonacci'''
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
		
def fib_iter(n):
	'''tail-recursive fibonacci'''
	def iter(n, acc, acc_prev):
		if n == 0:
			return acc
		else:
			return iter(n-1, acc+acc_prev, acc)
			
	return iter(n, 1, 0)
		
# sum of list

def sum(list):
	num_elements = len(list)
	
	def sum_iter(acc, count):
		if list == []:
			return 0

		if count > 0:
			return sum_iter(acc+list[count-1], count - 1)
		else:
			return acc
			
	return sum_iter(0, num_elements)		

# find last appearance of n in list, first by counting backwards then by counting forwards
	
def lastIndexOf_old(n, list):

	num_elem = len(list)
	
	def lastIndex_iter(count):
		if list == []:
			return -1
	
		if list[num_elem-1-count] == n:
			return num_elem-1-count
		elif count > num_elem:
			return -1
		else:
			return lastIndex_iter(count+1)
			
	return lastIndex_iter(0)
	
def lastIndexOf(n, list):

	def lastIndex_iter(lastindex, count):
			
		if list[count] == n:
			lastindex = count
		count = count+1
		if count != len(list):
			return lastIndex_iter(lastindex, count)
		else:
			return lastindex
	
	if list == []:
		return -1
	else:		
		return lastIndex_iter(-1,0)
		
# First make binary tree class, with depth-first and breadth-first searches
	
class Node(object):
	def __init__(self, value, l=None, r=None):
		self.value = value
		self.left = l
		self.right = r

class Tree(object):
	def __init__(self, root):
		self.root = root
		
	def printTree(self,dfs=True):
		if dfs: # assume stack
			s = Stack()
			node = self.root
			while not (node is None and s.isEmpty()):
				if node is None:
					node = s.pop()
					node = node.right
				else:
					print node.value
					s.push(node)
					node = node.left
		
		else:
			q = Queue()
			q.push(self.root)
			while not q.isEmpty():
			
				node = q.pop()
				print node.value
		
				if node.left is not None:
					q.push(node.left)
				if node.right is not None:
					q.push(node.right)


tree = Tree(Node(1, l=Node(2, l=Node(3), r=Node(4)), r=Node(5, l=Node(6), r=Node(7))))
othertree = Tree(Node(1, l=Node(2, l=Node(3, l=Node(4), r=Node(5)), r=Node(6)), r=Node(8, l=Node(9, l=Node(10), r=Node(11)), r=Node(12))))

# Then find sum of elements, recursively and tail-recursively

def sumTree(tree):

	def sum_elem(elem):
		if not elem.left:
			elem.left = 0
		if not elem.right:
			elem.right = 0
		if elem.left == 0 and elem.right == 0:
			return elem.value
		else:
			return elem.value + sum(elem.left) + sum(elem.right)
						
	return sum_elem(tree.root)
	

def sumTreeIter(tree):

	def sum_iter(acc, root, stack):
		acc += root.value
		if root.right is not None:
			stack.push(root.right)
		root = root.left
		if root is None:
			if stack.isEmpty():
				return acc
			else:
				root = stack.pop()
				return sum_iter(acc, root, stack)
		else:
			return sum_iter(acc, root, stack)	


	return sum_iter(0, tree.root, Stack())
	
# find permutations of the power set of a set (of letters)
	
def scrabble_all_words(letters):

	# all n letter words + all n-1 letter words + ...
	words = []
	def make_words(words, some_letters):
	
		for letter in some_letters:
#			pdb.set_trace()
			words.append(letter + make_words(words, some_letters.remove(letter)))
			print letter
			
	make_words(words, letters)
	return words
	
# Step Climbing: find combinations, recursively and tail-recursively

def count_ways_up_steps(n):

	def counter(nsteps, jump):
		if nsteps == 0:
			return 1
		elif nsteps < 0 or jump == 0:
			return 0
		else:
			return counter(nsteps, jump-1) + counter(nsteps - jump, jump)
			
	return counter(n, 3)
	
def count_steps_two(n):
	
	def count_iter(nsteps, jump, total):
		if nsteps == 0:
			total += 1
			return total
		elif nsteps < 0 or jump == 0:
			return total
		else:
			return count_iter(nsteps-jump, jump, count_iter(nsteps, jump-1, total))
			
	return count_iter(n,3,0)
	
# Project Euler 15: find combinations
	
def count_ways_through_city(ns_blocks, ew_blocks):

	def counter(ns, ew):
		if ns == 0 and ew == 0:
			return 1
		if ns < 0 or ew < 0:
			return 0
		else:
			return counter(ns-1, ew) + counter(ns, ew-1)
			
	return counter(ns_blocks-1, ew_blocks-1)
	
# Change-counting: done elsewhere

# Minimax of Tic Tac Toe: in tictactoe.py

# Graphs and Trees

# Difference between graphs and trees

# Difference between directed and undirected graphs

# Make a graph class

# Check accessibility

# subtree test

# recursive implementation of map

# recursive implementation of filter

# make new linked list with element e at location i

# in general, n choose k

# compute n choose k

# find power set of set

# find all partitions of a set
	

	

	
			
			
			
			
			