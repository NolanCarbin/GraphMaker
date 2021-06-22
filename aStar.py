from priorityQueue import PriorityQueue

def heuristic(startingNode, targetNode):
    x0, y0 = startingNode
    x1, y1 = targetNode
    return abs(x0 - x1) + abs(y0 - y1)


def aStar(app, graph, startingNode, targetNode):
    queue = PriorityQueue()
    queue.put(startingNode, 0)
    cameFrom = {}
    costSoFar = {}
    cameFrom[startingNode] = None
    costSoFar[startingNode] = 0

    while not queue.empty():
        current = queue.get()
        #for visualizer:
        app.aStarSearchQueue.append(current)
        ################
        if current == targetNode:
            return reconstructPath(cameFrom, startingNode, targetNode)
       
        for (neighborRow, neighborCol, weight) in graph[current]:
            neighborNode = (neighborRow, neighborCol)
            newCost = costSoFar[current] + weight
            if neighborNode not in costSoFar or newCost < costSoFar[neighborNode]:
                costSoFar[neighborNode] = newCost
                priority = newCost + heuristic(neighborNode, targetNode)
                queue.put(neighborNode, priority)
                cameFrom[neighborNode] = current
    return None

def reconstructPath(cameFrom, startingNode, targetNode):
    current = targetNode
    path = []
    while current != startingNode:
        path.append(current)
        current = cameFrom[current]
    path.append(startingNode)
    path.reverse()
    return path
