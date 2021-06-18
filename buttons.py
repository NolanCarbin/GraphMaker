from collections import deque
from graph import *
from bfs import *
from dfs import *

def inBounds(x, y, recX0, recY0, recX1, recY1):
    return (recX0 <= x <= recX1 and recY0 <= y <= recY1)
    
def inBoundsOfNodeButtons(app, event):
    #starting node button
    if inBounds(event.x, event.y, 20, 20, 40, 40): 
        app.movingStartingNode = not app.movingStartingNode
        if app.movingStartingNode:
            app.movingTargetNode = False
            app.movingWallNode = False
    #target node button
    if inBounds(event.x, event.y, 20, 60, 40, 80): 
        app.movingTargetNode = not app.movingTargetNode
        if app.movingTargetNode:
            app.movingStartingNode = False
            app.movingWallNode = False
    #wall node button
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
        restartApp(app)
    if inBounds(event.x, event.y, app.width-140, 80, app.width-20, 120):
        clearPath(app)

def restartApp(app):
    app.timerDelay = 50
    app.startingNode = (9,9)
    app.targetNode = (9,20)
    app.wallNodes = set()
    app.movingStartingNode = False
    app.movingTargetNode = False
    app.movingWallNode = False
    app.path = [ ]
    app.fastMode = False
    app.mediumMode = True
    app.slowMode = False
    app.bfsSearchQueue = deque()
    app.dfsSearchStack = deque()
    app.visualizedList = [ ]
    app.visualizedIndex = 0
    app.isVisualizing = False
    app.timer = 0

def clearPath(app):
    app.wallNodes = set()
    app.path = [ ]
    app.bfsSearchQueue = deque()
    app.dfsSearchStack = deque()
    app.visualizedList = [ ]
    app.visualizedIndex = 0
    app.isVisualizing = False

#Doesn't remove the current walling
def refreshForNewSearch(app):
    app.path = [ ]
    app.bfsSearchQueue = deque()
    app.dfsSearchStack = deque()
    app.visualizedList = [ ]
    app.visualizedIndex = 0
    app.isVisualizing = False
        

def inBoundsOfAlgoButtons(app, event):
    #bfs button
    if inBounds(event.x, event.y, 350, 20, 470, 60):
        refreshForNewSearch(app)
        graph = createAdjacencyList(initNodeList(app), 1)
        app.path = bfsSearch(app, graph, app.startingNode, app.targetNode)
        if app.path != None:
            app.isVisualizing = True
    #dfs button
    elif inBounds(event.x, event.y, 500, 20, 620, 60):
        refreshForNewSearch(app)
        graph = createAdjacencyList(initNodeList(app), 1)
        app.path = dfsSearch(app, graph, app.startingNode, app.targetNode)
        if app.path != None:
            app.isVisualizing = True
    #dijkstras button
    elif inBounds(event.x, event.y, 350, 80, 470, 120):
        refreshForNewSearch(app)
        # graph = createAdjacencyList(initNodeList(app), 1)
        # app.path = dfsSearch(app, graph, app.startingNode, app.targetNode)
        # if app.path != None:
            # app.isVisualizing = True
        print('dijkstra')
    #A* button
    elif inBounds(event.x, event.y, 500, 80, 620, 120):
        refreshForNewSearch(app)
        # graph = createAdjacencyList(initNodeList(app), 1)
        # app.path = dfsSearch(app, graph, app.startingNode, app.targetNode)
        # if app.path != None:
            # app.isVisualizing = True
        print('A*')

        

######################
# Draw functions
######################

def drawNodeButtons(app, canvas):
    #starting node nutton
    if app.movingStartingNode:
        startingNodeColor = 'blue'
    else:
        startingNodeColor = 'white'
    canvas.create_rectangle(20, 20, 40, 40, fill=startingNodeColor)
    canvas.create_text(50, 30, text='Starting Node', anchor='w')

    #target node button
    if app.movingTargetNode:
        targetNodeColor = 'green'
    else:
        targetNodeColor = 'white'
    canvas.create_rectangle(20, 60, 40, 80, fill=targetNodeColor)
    canvas.create_text(50, 70, text='Target Node', anchor='w')

    #wall node button
    if app.movingWallNode:
        wallNodeColor = 'black'
    else:
        wallNodeColor = 'white'
    canvas.create_rectangle(20, 100, 40, 120, fill=wallNodeColor)
    canvas.create_text(50, 110, text='Wall Node', anchor='w')

def drawCreateMazeButton(app, canvas):
    pass

def drawAlgorithmButtons(app, canvas):
    #bfs button
    canvas.create_rectangle(350, 20, 470, 60)
    canvas.create_text(410, 40, text='BFS')
    #dfs button
    canvas.create_rectangle(500, 20, 620, 60)
    canvas.create_text(560, 40, text='DFS')
    #dijkstras button
    canvas.create_rectangle(350, 80, 470, 120)
    canvas.create_text(410, 100, text='Dijkstra')
    #A* button
    canvas.create_rectangle(500, 80, 620, 120)
    canvas.create_text(560, 100, text='A*')

def drawResetButtons(app, canvas):
    #reset button
    canvas.create_rectangle(app.width-140, 20, app.width-20, 60)
    canvas.create_text(app.width-80, 40, text='Reset')
    #clear path button
    canvas.create_rectangle(app.width-140, 80, app.width-20, 120)
    canvas.create_text(app.width-80, 100, text='Clear Path')

def drawSpeedButtons(app, canvas):
    #fast speed button
    if app.fastMode:
        fastModeColor = 'black'
    else:
        fastModeColor = 'white'
    canvas.create_rectangle(app.width - 300, 20, app.width - 280, 40, fill=fastModeColor)
    canvas.create_text(app.width - 270, 30, text='Fast', anchor='w')
    #medium speed button
    if app.mediumMode:
        mediumModeColor = 'black'
    else:
        mediumModeColor = 'white'
    canvas.create_rectangle(app.width - 300, 60, app.width - 280, 80, fill=mediumModeColor)
    canvas.create_text(app.width - 270, 70, text='Medium', anchor='w')
    #slow speed button
    if app.slowMode:
        slowModeColor = 'black'
    else:
        slowModeColor = 'white'
    canvas.create_rectangle(app.width - 300, 100, app.width - 280, 120, fill=slowModeColor)
    canvas.create_text(app.width - 270, 110, text='Slow', anchor='w')
