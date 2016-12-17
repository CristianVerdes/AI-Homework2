import random
class Node:
    def __init__(self):
        self.node = -1
        self.neighbours = []
        self.color = ""
        self.possibleColors = ["red" , "green", "blue"]

    def updateState(self, node, neighbours):
        self.node = node
        self.neighbours = neighbours

    #Setters
    def addRestrictions(self, restrictions):
        self.restrictions = restrictions

    def addColor(self, color):
        self.color = color

    def addRandomColor(self):
        self.color = random.choice(self.possibleColors)
        self.possibleColors.remove(self.color)

    #Getters
    def getColor(self):
        return self.color

    def getNeighbours(self):
        return self.neighbours;

    def getPossibleColors(self):
        return self.possibleColors
class Graph:
    def __init__(self):
        self.graph = []
        self.fitness = -1
        self.oldState = []
        self.oldFitness = -1

    def addNode(self, node):
        self.graph.append(node)

    def isValidGraph(self):
        for node in self.graph:
            for neighbour in node.getNeighbours():
                if node.getColor() == self.graph[neighbour].getColor():
                    return False
        return True

    # First Node conflict
    def firstConflict(self):
        for node in self.graph:
            for neighbour in node.getNeighbours():
                if node.getColor() == self.graph[neighbour].getColor():
                    return node

    # Modify graph with first node conflict
    def modifyGraphWithFirstNodeConflict(self):
        self.changeNodeColor(self.firstConflict())

    # Change all graph
    def changeGraph(self):
        for node in self.graph:
            for neighbour in node.getNeighbours():
                if node.getColor() == self.graph[neighbour].getColor():
                    self.changeNodeColor(node)

    # Change Node color
    def changeNodeColor(self, node):
        node = self.getNode(node)
        node.addColor(random.choice(node.getPossibleColors()))

    # Getters
    def getNode(self, node):
        return self.graph[self.graph.index(node)]
    def getGraph(self):
        return self.graph
    def getGraphFitness(self):
        return self.fitness

    # FITNESS
    def computeGraphFitness(self):
        self.fitness = 0
        for node in self.graph:
            goodNode = True
            for neighbour in node.getNeighbours():
                if node.getColor() == self.graph[neighbour].getColor():
                    goodNode = False
            if goodNode:
                self.fitness += 1

    # Print
    def printGraph(self):
        for node in self.graph:
            print("Node: ", node.node)
            #print("Neighbours: ", node.neighbours)
            #print("Possible Colors: ", node.possibleColors)
            print("Color: ", node.color)
            print()

    # Save and restore Graph
    def saveCurrentStateGraph(self):
        self.oldState = self.graph
        self.oldFitness = self.fitness

    def restoreOldStateGraph(self):
        self.graph = self.oldState
        self.fitness = self.oldFitness
class States:
    def __init__(self):
        self.fitness = []
        self.states = []

    def getMinState(self, fitness):
        position = self.fitness.index(min(self.fitness))
        return self.states[position]


def mySolution(graph):
    while True:
        if graph.isValidGraph() != True:
            print("GRAPH__________________________ FITNESS: ", graph.getGraphFitness())
            print(graph.printGraph())
            graph.changeGraph()
            graph.computeGraphFitness()

        else:
            break


def minConflicts(graph):
    while True:
        if graph.isValidGraph() != True:
            print("GRAPH__________________________ FITNESS: ", graph.getGraphFitness())
            print(graph.printGraph())
            # Create all states from curent state for graph

            # Choose the state with the lowest impact on the Graph fitness

            graph

def main():
    # Build Graph
    graph = Graph()

    node0 = Node()
    node0.updateState(0, [1, 5])
    node0.addRandomColor()
    graph.addNode(node0)

    node1 = Node()
    node1.addRandomColor()
    node1.updateState(1, [0, 2, 5])
    graph.addNode(node1)

    node2 = Node()
    node2.addRandomColor()
    node2.updateState(2, [1, 3, 5])
    graph.addNode(node2)

    node3 = Node()
    node3.addRandomColor()
    node3.updateState(3, [2, 4, 5])
    graph.addNode(node3)

    node4 = Node()
    node4.addRandomColor()
    node4.updateState(4, [3, 5])
    graph.addNode(node4)

    node5 = Node()
    node5.addRandomColor()
    node5.updateState(5, [0, 1, 2, 3, 4])
    graph.addNode(node5)

    node6 = Node()
    node6.addRandomColor()
    node6.updateState(6, [])
    graph.addNode(node6)

    # My solution
    # Problem: it can get to a state with a lower fitness that the one before
    mySolution(graph)

    # Min- Conflicts
    # minConflicts(graph)

    # Last Graph
    print("GRAPH__________________________ FITNESS: ", graph.getGraphFitness())
    print(graph.printGraph())

main()
