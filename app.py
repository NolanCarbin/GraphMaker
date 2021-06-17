from cmu_112_graphics import *
from collections import deque
from grid import *
from graph import *
from bfs import *


def appStarted(app):
    app.timerDelay = 50

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

    app.fastMode = False
    app.mediumMode = True
    app.slowMode = False

    app.bfsSearchQueue = deque()
    app.visualizedQueue = deque()
    app.visualizedIndex = 0
    app.isVisualizing = False
    
    app.timer = 0
    

def appStopped(app):
    pass

def mousePressed(app, event):
    inBoundsOfResetButtons(app, event)
    inBoundsOfSpeedButtons(app, event)
    if not app.isVisualizing:
        moveNodes(app, event)
        inBoundsOfNodeButtons(app, event)
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

def inBoundsOfSpeedButtons(app, event):
    #fast speed
    if inBounds(event.x, event.y, app.width - 300, 20, app.width - 280, 40):
        print('fast')
        app.timerDelay = 0 
        app.fastMode = True
        if app.fastMode:
            app.mediumMode = False
            app.slowMode = False
    #medium speed
    if inBounds(event.x, event.y, app.width - 300, 60, app.width - 280, 80): 
        print('md')
        app.timerDelay = 35 
        app.mediumMode = True
        if app.mediumMode:
            app.fastMode = False
            app.slowMode = False
    #slow speed
    if inBounds(event.x, event.y, app.width - 300, 100, app.width - 280, 120): 
        print('slow')
        app.timerDelay = 100 
        app.slowMode = True
        if app.slowMode:
            app.fastMode = False
            app.mediumMode = False
    
def inBoundsOfResetButtons(app, event):
    if inBounds(event.x, event.y, app.width-140, 20, app.width-20, 60):
        appStarted(app)
    if inBounds(event.x, event.y, app.width-140, 80, app.width-20, 120):
        app.wallNodes = set()
        app.currentPath = [ ]
        app.bfsSearchQueue = deque()
        app.visualizedQueue = deque()
        app.visualizedIndex = 0
        app.isVisualizing = False
        

def inBoundsOfAlgoButtons(app, event):
    if inBounds(event.x, event.y, 300, 20, 420, 60):
        graph = createAdjacencyList(initNodeList(app), 1)
        app.currentPath = bfsSearch(app, graph,app.startingNode,app.targetNode)
        if app.currentPath != None:
            app.isVisualizing = True

    elif inBounds(event.x, event.y, 500, 20, 620, 60):
        graph = createAdjacencyList(initNodeList(app), 1)
        print('dfs')

def keyPressed(app, event):
    pass

def timerFired(app):
    # app.timer += 1
    bfsVisualizer(app)
    

def bfsVisualizer(app):
    if app.currentPath != None:
        if len(app.bfsSearchQueue) >= 1:
            if app.visualizedIndex < len(app.bfsSearchQueue) - 1:
                app.visualizedIndex += 1
                app.visualizedQueue.append(app.bfsSearchQueue[app.visualizedIndex])
            else:
                app.isVisualizing = False

# def isOneSecond(app):
#     return app.timer % 10 == 0


def redrawAll(app, canvas):
    drawGrid(app, canvas)
    drawVisualizedQueue(app, canvas)
    if not app.isVisualizing:
        drawCurrentPath(app, canvas)
    drawStartingNode(app, canvas)
    drawTargetNode(app, canvas)
    drawWallNodes(app, canvas)
    drawNodeButtons(app, canvas)
    drawAlgorithmButtons(app, canvas)
    drawResetButtons(app, canvas)
    drawSpeedButtons(app, canvas)

    
    
def drawVisualizedQueue(app, canvas):
    if len(app.visualizedQueue) >= 1:
        for row, col in app.visualizedQueue:
            x0,y0,x1,y1 = getCellBounds(app, row, col)
            canvas.create_rectangle(x0,y0,x1,y1,fill='light blue')

def drawCurrentPath(app, canvas):
    if app.currentPath == None: return
    for row, col in app.currentPath:
        x0,y0,x1,y1 = getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill='yellow')



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

def drawSpeedButtons(app, canvas):
    if app.fastMode:
        fastModeColor = 'black'
    else:
        fastModeColor = 'white'
    canvas.create_rectangle(app.width - 300, 20, app.width - 280, 40, fill=fastModeColor)
    canvas.create_text(app.width - 270, 30, text='Fast', anchor='w')

    if app.mediumMode:
        mediumModeColor = 'black'
    else:
        mediumModeColor = 'white'
    canvas.create_rectangle(app.width - 300, 60, app.width - 280, 80, fill=mediumModeColor)
    canvas.create_text(app.width - 270, 70, text='Medium', anchor='w')

    if app.slowMode:
        slowModeColor = 'black'
    else:
        slowModeColor = 'white'
    canvas.create_rectangle(app.width - 300, 100, app.width - 280, 120, fill=slowModeColor)
    canvas.create_text(app.width - 270, 110, text='Slow', anchor='w')


runApp(width=1000, height=600)