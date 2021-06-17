from collections import deque


def bfsSearch(app, graph, startingNode, targetNode):
    queue = deque()
    cameFrom = dict()
    cameFrom[startingNode] = None
    queue.append(startingNode)
    #used for visualizer:
    app.bfsSearchQueue.append(startingNode)
    #####################
    while len(queue) != 0:
        currentNode = queue.popleft()
        #used for visualizer:
        app.bfsSearchQueue.append(currentNode)
        #####################
        if currentNode == targetNode:
            return path(startingNode, currentNode, cameFrom)
        for node in graph[currentNode]:
            if node not in cameFrom:
                cameFrom[node] = currentNode
                queue.append(node)
    return None

def path(startingNode, currentNode, cameFrom):
    endPath = []
    while currentNode != startingNode:
        endPath.append(currentNode)
        currentNode = cameFrom[currentNode]
        endPath.append(startingNode)
    endPath.reverse()
    return endPath
