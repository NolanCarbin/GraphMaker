def initNodeList(app):
    nodeList = []
    for row in range(app.rows):
        for col in range(app.cols):
            if (row, col) not in app.wallNodes:
                nodeList.append((row,col))
    return nodeList


#interval for using cells is 1
def createAdjacencyList(L, interval):
    def isEdge(row1, col1, row2, col2, interval):
        return ((abs(row1 - row2) == 0 and abs(col1 - col2) == interval) or 
                (abs(row1 - row2) == interval and abs(col1 - col2) == 0))
    graph = dict()
    for nodeRow, nodeCol in L:
        graph[(nodeRow, nodeCol)] = set()
        for edgeRow, edgeCol in L:
            if (nodeRow, nodeCol) != (edgeRow, edgeCol):
                if isEdge(nodeRow, nodeCol, edgeRow, edgeCol, interval):
                    graph[(nodeRow, nodeCol)].add((edgeRow, edgeCol))        
    return graph




#[(row, col, weight=1)] default 1 weight
def initWeightedNodeList(app):
    nodeList = []
    for row in range(app.rows):
        for col in range(app.cols):
            if (row, col) not in app.wallNodes:
                nodeList.append((row,col,1))
    return nodeList


# Node        connected node     connected node
#(row, col): {(row,col,weight), (row, col, weight)}
exampleAdjList = {
    (0,0): {(0,1,2), (1,0,1)},
    (0,1): {(0,0,1), (0,2,1)}
}

def createWeightedAdjacencyList(L, interval):
    def isEdge(row1, col1, row2, col2, interval):
        return ((abs(row1 - row2) == 0 and abs(col1 - col2) == interval) or 
                (abs(row1 - row2) == interval and abs(col1 - col2) == 0))
    graph = dict()
    for nodeRow, nodeCol, nodeWeight in L:
        graph[(nodeRow, nodeCol)] = set()
        for edgeRow, edgeCol, edgeWeight in L:
            if (nodeRow, nodeCol) != (edgeRow, edgeCol):
                if isEdge(nodeRow, nodeCol, edgeRow, edgeCol, interval):
                    graph[(nodeRow, nodeCol)].add((edgeRow, edgeCol, edgeWeight))        
    return graph

