
def getWeight(side):
    return side[1]

class Graph:
    def __init__(self):
        self.points = []
        self.list = {}

    def addPoint(self, pointName):
        if pointName not in self.list:
            self.points.append(pointName)
            self.list[pointName] = []

    def addSide(self, point1, point2, weight):

        if point1 not in self.list:
            print("First vertex missing")
            return

        if point2 not in self.list:
            print("Second vertex missing")
            return

        self.list[point1].append((point2, weight))
        self.list[point2].append((point1,weight))
        self.list[point1].sort(key=getWeight)
        self.list[point2].sort(key=getWeight)

    def graphPrint(self):
        print("\n\n")

        print("GRAPH\n")
        for p in self.points:
            print(p, ">>>", self.list[p])

    def DFS(self, start):
        visited = []

        def helper(node):
            visited.append(node)
            print(node)

            for neighbor in self.list[node]:
                nextNode = neighbor[0]
                if nextNode not in visited:
                    helper(nextNode)

        print("\nDepth first:")
        helper(start)

    def BFS(self, start):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        print("\nBredth first:")

        while len(queue) > 0:
            current = queue.pop(0)
            print(current)

            for neighbor in self.list[current]:
                nextNode = neighbor[0]
                if nextNode not in visited:
                    visited.append(nextNode)
                    queue.append(nextNode)

g = Graph()

g.addPoint("Cardassian Union")
g.addPoint("Romulan Empire")
g.addPoint("Bajoran")
g.addPoint("United Federation of Planets")
g.addPoint("Tholian Assembly")
g.addPoint("Klingon Empire")
g.addPoint("Borg")
g.addSide("Cardassian Union", "Romulan Empire", 42)
g.addSide("Cardassian Union", "Bajoran", 14)
g.addSide("Romulan Empire", "United Federation of Planets", 53)
g.addSide("Bajoran", "United Federation of Planets", 22)
g.addSide("Bajoran", "Tholian Assembly", 80)
g.addSide("United Federation of Planets", "Klingon Empire", 87)
g.addSide("Tholian Assembly", "Borg", 10)
g.addSide("Romulan Empire", "Borg", 33)
g.addSide("Klingon Empire", "Borg", 41)

g.graphPrint()

print("\nwhere would you like to start depth first from: ")
start = input()
g.DFS(start)

print("\nwhere would you like to start bredth first from: ")
start = input()
g.BFS(start)
