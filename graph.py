def initNodeList(app):
    nodeList = []
    for row in range(app.rows):
        for col in range(app.cols):
            if (row, col) not in app.wallNodes:
                nodeList.append((row,col))
    return nodeList


#interval for using cells is 1
def createAdjacencyList(L, interval):
    def isEdge(x0, y0, x1, y1, interval):
        return ((abs(x0 - x1) == 0 and abs(y0 - y1) == interval) or 
                (abs(x0 - x1) == interval and abs(y0 - y1) == 0))
    graph = dict()
    for nodeRow, nodeCol in L:
        graph[(nodeRow, nodeCol)] = set()
        for edgeRow, edgeCol in L:
            if (nodeRow, nodeCol) != (edgeRow, edgeCol):
                if isEdge(nodeRow, nodeCol, edgeRow, edgeCol, interval):
                    graph[(nodeRow, nodeCol)].add((edgeRow, edgeCol))        
    return graph