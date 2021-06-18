from collections import deque

def dfsSearch(app, graph, startingNode, targetNode):
    stack = deque()
    stack.append(startingNode)
    visited = set()
    #used for visualizer:
    app.dfsSearchStack.append(startingNode)
    #####################
    cameFrom = dict()
    cameFrom[startingNode] = None
    while len(stack) != 0:
        currentNode = stack.pop()
        #used for visualizer:
        app.dfsSearchStack.append(currentNode)
        #####################
        if currentNode not in visited:
            visited.add(currentNode)
            for node in graph[currentNode]:
                if node not in cameFrom:
                    cameFrom[node] = currentNode
                if node == targetNode:
                    return dfsPath(startingNode, node, cameFrom)
                stack.append(node)
    return None


def dfsPath(startingNode, currentNode, cameFrom):
    endPath = []
    while currentNode != startingNode:
        endPath.append(currentNode)
        currentNode = cameFrom[currentNode]
        endPath.append(startingNode)
    endPath.reverse()
    return endPath