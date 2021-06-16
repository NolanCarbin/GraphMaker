from cmu_112_graphics import *
from grid import *
from graph import *
from bfs import *


def appStarted(app):
    app.rows = 20
    app.cols = 30
    app.xMargin = 10
    app.yMarginTop = 150
    app.yMarginBottom = 10
    app.startingNode = (9,9)
    app.targetNode = (9,20)
    app.wallNodes = set()
    app.movingStartingNode = False
    app.movingTargetNode = False
    app.movingWallNode = False
    app.currentPath = []

def appStopped(app):
    pass

def mousePressed(app, event):
    moveNodes(app, event)
    inBoundsOfNodeButtons(app, event)
    inBoundsOfResetButtons(app, event)
    inBoundsOfAlgoButtons(app, event)

def moveNodes(app, event):
    currentNode = getCell(app, event.x, event.y)
    #toggles moving flag for the nodes if clicked on
    if currentNode == app.startingNode: 
        app.movingStartingNode = True
        app.movingTargetNode = False
        app.movingWallNode = False
    elif currentNode == app.targetNode: 
        app.movingTargetNode = True
        app.movingStartingNode = False
        app.movingWallNode = False

    #logic that moves the nodes
    if currentNode != None:
        if app.movingStartingNode:
            if currentNode in app.wallNodes:
                app.wallNodes.remove(currentNode)
            app.startingNode = currentNode 
        elif app.movingTargetNode:
            if currentNode in app.wallNodes:
                app.wallNodes.remove(currentNode)
            app.targetNode = currentNode
        elif app.movingWallNode:
            if currentNode in app.wallNodes:
                app.wallNodes.remove(currentNode)
            elif currentNode == app.startingNode or currentNode == app.targetNode:
                return
            else:
                app.wallNodes.add((currentNode))

def inBounds(x, y, recX0, recY0, recX1, recY1):
    return (recX0 <= x <= recX1 and recY0 <= y <= recY1)
    
def inBoundsOfNodeButtons(app, event):
    # (20, 20, 40, 40) starting node button
    if inBounds(event.x, event.y, 20, 20, 40, 40): 
        app.movingStartingNode = not app.movingStartingNode
        if app.movingStartingNode:
            app.movingTargetNode = False
            app.movingWallNode = False
    # (20, 60, 40, 80) target node button
    if inBounds(event.x, event.y, 20, 60, 40, 80): 
        app.movingTargetNode = not app.movingTargetNode
        if app.movingTargetNode:
            app.movingStartingNode = False
            app.movingWallNode = False
    # (20, 100, 40, 120) wall node button
    if inBounds(event.x, event.y, 20, 100, 40, 120): 
        app.movingWallNode = not app.movingWallNode
        if app.movingWallNode:
            app.movingStartingNode = False
            app.movingTargetNode = False
    
def inBoundsOfResetButtons(app, event):
    if inBounds(event.x, event.y, app.width-140, 20, app.width-20, 60):
        appStarted(app)
    if inBounds(event.x, event.y, app.width-140, 80, app.width-20, 120):
        app.wallNodes = set()
        app.currentPath = [ ]

def inBoundsOfAlgoButtons(app, event):
    if inBounds(event.x, event.y, 300, 20, 420, 60):
        graph = createAdjacencyList(initNodeList(app), 1)
        app.currentPath = bfsSearch(graph,app.startingNode,app.targetNode)

    elif inBounds(event.x, event.y, 500, 20, 620, 60):
        print('dfs')

def keyPressed(app, event):
    pass

def timerFired(app):
    pass


def redrawAll(app, canvas):
    drawGrid(app, canvas)
    drawCurrentPath(app, canvas)
    drawStartingNode(app, canvas)
    drawTargetNode(app, canvas)
    drawWallNodes(app, canvas)
    drawNodeButtons(app, canvas)
    drawAlgorithmButtons(app, canvas)
    drawResetButtons(app, canvas)
    


def drawNodeButtons(app, canvas):
    if app.movingStartingNode:
        startingNodeColor = 'blue'
    else:
        startingNodeColor = 'white'
    canvas.create_rectangle(20, 20, 40, 40, fill=startingNodeColor)
    canvas.create_text(50, 30, text='Starting Node', anchor='w')

    if app.movingTargetNode:
        targetNodeColor = 'green'
    else:
        targetNodeColor = 'white'
    canvas.create_rectangle(20, 60, 40, 80, fill=targetNodeColor)
    canvas.create_text(50, 70, text='Target Node', anchor='w')

    if app.movingWallNode:
        wallNodeColor = 'black'
    else:
        wallNodeColor = 'white'
    canvas.create_rectangle(20, 100, 40, 120, fill=wallNodeColor)
    canvas.create_text(50, 110, text='Wall Node', anchor='w')

def drawAlgorithmButtons(app, canvas):
    canvas.create_rectangle(300, 20, 420, 60)
    canvas.create_text(360, 40, text='BFS')
    canvas.create_rectangle(500, 20, 620, 60)
    canvas.create_text(560, 40, text='DFS')

def drawResetButtons(app, canvas):
    canvas.create_rectangle(app.width-140, 20, app.width-20, 60)
    canvas.create_text(app.width-80, 40, text='Reset')
    canvas.create_rectangle(app.width-140, 80, app.width-20, 120)
    canvas.create_text(app.width-80, 100, text='Clear Path')

def drawCurrentPath(app, canvas):
    if app.currentPath == None: return
    for row, col in app.currentPath:
        x0,y0,x1,y1 = getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill='yellow')

runApp(width=1000, height=600)