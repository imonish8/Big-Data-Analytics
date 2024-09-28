class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Linkedlist:
	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		# we are putting assiging head and tail new_node becasue this single element linkedlist.
		self.length = 1
		

new_Linkedlist = Linkedlist(20)
print(new_Linkedlist)
print(new_Linkedlist.head)
print(new_Linkedlist.tail)
print(new_Linkedlist.head.value)
print(new_Linkedlist.length)
		
