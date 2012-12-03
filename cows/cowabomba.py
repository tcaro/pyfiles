#!/usr/bin/python3

'''
Title: cowabomba.py
Language: python3
Assignment: Lab 01
Author: Troy Caro <twc9438@rit.edu>
Date: November 28, 2012
Purpose: Given a starting bomb, determine the sequence of bombs and cows that are involved in the chain reaction.
'''

#####################################################################################################################
# DATA STRUCTURES
#####################################################################################################################

class Node():
	"""
	Node represents a node in the graph using adjacency lists.
		Node.id is a String.
		Node.name is a String.
		Node.x is an Integer.
		Node.y is an Integer.
		Node.r is an Integer.
		Node.neighbors is a list of nodes.
	"""
	__slots__ = ('id', 'name', 'x', 'y', 'r', 'neighbors')
	
	def __init__(self, id, name, x, y, r):
		"""
		___init___: Constructs a Node object with the given id, name, x, y, and r, and no neighbors.
		"""
		self.id = id
		self.name = name
		self.x = x
		self.y = y
		if "cow" in id:
			self.r = 0
		else:
			self.r = r
		self.neighbors = []
	
	def __str__(self):
		"""
		Returns a string with the id, name, x y and r values of the node, and the nodes neighbors.
		"""
		if "cow" in self.id:
			total = str(self.id) + " " + str(self.name) + " " + str(self.x) + " " + str(self.y) + ": "
		else:
			total = str(self.id) + " " + str(self.name) + " " + str(self.x) + " " + str(self.y) + " " + str(self.r) + ": "

		
		if len(self.neighbors) > 0:
			for x in range( len( self.neighbors) - 1 ):
				total += str(self.neighbors[x].id) + " " + str(self.neighbors[x].name) + " " + str(self.neighbors[x].x) + " " + \
							str(self.neighbors[x].y) + " " + str(self.neighbors[x].r) + " - "
			total += str(self.neighbors[-1].id) + " " + str(self.neighbors[-1].name) + " " + str(self.neighbors[-1].x) + " " + \
						str(self.neighbors[-1].y) + " " + str(self.neighbors[-1].r)
		
		return total

#####################################################################################################################
# UTILITY FUNCTIONS
#####################################################################################################################

def loadGraph(fileName):
	"""
	Loads graph data from the file with the given id, name, x y and r values.
	
	Parameters:
		fileName (string) - the name of the file containing the graph data
	Pre-conditions:
		file content is well-formed, and properly formatted.
	"""
	graph = {}
	
	for line in open(fileName):
		data = line.split()
		graph[ data[1] ] = Node( data[0], data[1], int( data[2] ), int( data[3] ), int( data[-1] ) )
	
	return graph
	
def printGraph(graph):
	"""
	Prints a graph by printing each one of its nodes.
	"""
	for x in graph:
		print( graph[x] )
		
#####################################################################################################################
# NODE FUNCTIONS
#####################################################################################################################

def inRange(node1, node2):
	"""
	Uses the distance formula to decide if the second node is within
	the radius of the first node.
	"""
	distance = ( ( (node1.x - node2.x)**(2) ) + ( (node1.y - node2.y)**(2) ) ) ** (1 / 2)
	if distance <= node1.r:
		return True
	else:
		return False
	
def buildNeighbors(graph):
	"""
	Given a graph of data, using the inRange function, this function will build 
	the chain reaction caused from each bomb.
	"""
	for key in graph:
		if "cow" in graph[key].id:
			pass
		else:
			for x in graph:
				if key == x:
					pass
				elif inRange( graph[key], graph[x] ):
					graph[key].neighbors.append( graph[x] )

#####################################################################################################################
# MAIN FUNCTION
#####################################################################################################################

def main():
	"""
	The program prompts for the file containing the graph data, then outputs
	the chain reaction that would happen using each bomb as a starting point.
	"""
	# read the data file:
	fileName = input( 'Enter the file containing the cow and bomb data: ' )
	if fileName == '':
		return
	graph = loadGraph( fileName )
	
	# build the neighbors
	buildNeighbors( graph )
	
	# print the graph data:
	printGraph( graph )
	
# runs the program
if __name__ == "__main__":
	main()