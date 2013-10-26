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
		

class LLNode:

	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		
	def AddNode(self, data):
		new_node = LLNode(data)
		if self.head == None:
			self.head = new_node
		
		if self.tail != None:
			self.tail.next = new_node
			
		self.tail = new_node
		
	def FindNode(self, index):
		prev = None
		node = self.head
		i = 0
		
		while node != None and i < index:
			prev = node
			node = node.next
			i += 1
		return node
		
	def RemoveNode(self, index):
		prev = None
		node = self.head
		i = 0
		
		while node != None and i < index:
			prev = node
			node = node.next
			i += 1
			
		if prev == None:
			self.head = node.next
		else:
			prev.next = node.next
			
		return node
		
	def InsertNode(self, node, index_of):
		first_tail = self.FindNode(index_of-1)
		second_head = first_tail.next
		first_tail.next = node
		node.next = second_head
	
	def PrintList(self):
		node = self.head
		while node != None:
			print node.data
			node = node.next
			
	def ReverseList(self):
		prev = None
		node = self.head
		
		while node != self.tail:
			newnext = prev
			prev = node
			node = node.next
			prev.next = newnext
			
		if node == self.tail:
			node.next = prev
		
		head = self.head
		self.head = self.tail
		self.tail = head
			
	
class BST_Node:
	
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None	
			
class BST:

	def __init__(self):
		self.root = None

	def Search(self, x):
		node = self.root
		done = False
		while done == False:
			if node == None:
				node = None
				done = True
			elif node.key == x:
				node = node
				done = True
			elif node.key < x:
				node = node.right
			elif node.key > x:
				node = node.left
		return node

	def AddNode(self, key):
		if self.root == None:
			self.root = BST_Node(key)
		else:
			node = self.root
			child = self.root
			while node != None and child != None:
				if node.key == key:
					child = None
				else:
					parent = node
					if key < node.key:
						node = node.left
					else:
						node = node.right
			if child != None:
				child = BST_Node(key)
				if key < parent.key:
					parent.left = child
				else:
					parent.right = child
					
	def PrintLeftTree(self):
		node = self.root
		while node:
			print node.key
			node = node.left
			
	def PrintRightTree(self):
		node = self.root
		while node:
			print node.key
			node = node.right
			
	def PrintTree(self):
		nodes = [self.root]
		while nodes != []:
			newnodes = []
			out = ''
			for node in nodes:
				out=out+str(node.key)+' '
				if node.left != None:
					newnodes.append(node.left)
				if node.right != None:
					newnodes.append(node.right)
			print out
			nodes = newnodes
			print '\n'
			
	def TreeInOrder(self):
		stack = Stack()
		current = self.root
		done = False
		while not done:
			if current is not None:	
				stack.push(current)
				current = current.left
			else:
				if stack.isEmpty():
					done = True
				else:
					current = stack.peek()
					print stack.pop().key
					current = current.right
			
bst = BST()
bst.AddNode(8)
bst.AddNode(4)
bst.AddNode(12)
bst.AddNode(2)
bst.AddNode(6)
bst.AddNode(10)
bst.AddNode(14)
bst.AddNode(1)
bst.AddNode(3)
bst.AddNode(5)
bst.AddNode(7)
bst.AddNode(9)
bst.AddNode(11)
bst.AddNode(13)
bst.AddNode(15)