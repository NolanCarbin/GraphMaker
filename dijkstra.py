from priorityQueue import PriorityQueue

def dijkstraSearch(graph, startingNode, targetNode):
    queue = PriorityQueue()
    queue.put(startingNode, 0)
    cameFrom = {}
    costSoFar = {}
    cameFrom[startingNode] = None
    costSoFar[startingNode] = 0

    while not queue.empty():
        current = queue.get()
        if current == targetNode:
            break
       
        for (neighborRow, neighborCol, weight) in graph[current]:
            neighborNode = (neighborRow, neighborCol)
            newCost = costSoFar[current] + weight
            if neighborNode not in costSoFar or newCost < costSoFar[neighborNode]:
                costSoFar[neighborNode] = newCost
                priority = newCost
                queue.put(neighborNode, priority)
                cameFrom[neighborNode] = current

    return cameFrom

def reconstructPath(cameFrom, startingNode, targetNode):
    current = targetNode
    path = []
    while current != startingNode:
        path.append(current)
        current = cameFrom[current]
    path.append(startingNode)
    path.reverse()
    return path
