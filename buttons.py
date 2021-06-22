from collections import deque
from graph import *
from intToColor import intToColor
from bfs import *
from dfs import *
from dijkstra import *
from aStar import *

def inBounds(x, y, recX0, recY0, recX1, recY1):
    return (recX0 <= x <= recX1 and recY0 <= y <= recY1)
    
def inBoundsOfNodeButtons(app, event):
    #starting node button
    if inBounds(event.x, event.y, 20, 20, 40, 40): 
        app.movingStartingNode = not app.movingStartingNode
        if app.movingStartingNode:
            app.movingTargetNode = False
            app.movingWallNode = False

            app.movingWeightNode1 = False
            app.movingWeightNode3 = False
            app.movingWeightNode7 = False
            app.movingWeightNodeC = False
    #target node button
    if inBounds(event.x, event.y, 20, 60, 40, 80): 
        app.movingTargetNode = not app.movingTargetNode
        if app.movingTargetNode:
            app.movingStartingNode = False
            app.movingWallNode = False

            app.movingWeightNode1 = False
            app.movingWeightNode3 = False
            app.movingWeightNode7 = False
            app.movingWeightNodeC = False
    #wall node button
    if inBounds(event.x, event.y, 20, 100, 40, 120): 
        app.movingWallNode = not app.movingWallNode
        if app.movingWallNode:
            app.movingStartingNode = False
            app.movingTargetNode = False

            app.movingWeightNode1 = False
            app.movingWeightNode3 = False
            app.movingWeightNode7 = False
            app.movingWeightNodeC = False

def inBoundsOfWeightButtons(app, event):
    #weight node 1
    if inBounds(event.x, event.y, 150, 20, 170, 40): 
        app.movingWeightNode1 = not app.movingWeightNode1
        if app.movingWeightNode1:
            app.movingStartingNode = False
            app.movingTargetNode = False
            app.movingWallNode = False

            app.movingWeightNode3 = False
            app.movingWeightNode7 = False
            app.movingWeightNodeC = False
    #Weight Node 3
    if inBounds(event.x, event.y, 150, 60, 170, 80): 
        app.movingWeightNode3 = not app.movingWeightNode3
        if app.movingWeightNode3:
            app.movingStartingNode = False
            app.movingTargetNode = False
            app.movingWallNode = False

            app.movingWeightNode1 = False
            app.movingWeightNode7 = False
            app.movingWeightNodeC = False
    #Weight Node 7
    if inBounds(event.x, event.y, 150, 100, 170, 120): 
        app.movingWeightNode7 = not app.movingWeightNode7
        if app.movingWeightNode7:
            app.movingStartingNode = False
            app.movingTargetNode = False
            app.movingWallNode = False

            app.movingWeightNode3 = False
            app.movingWeightNode1 = False
            app.movingWeightNodeC = False
    #custom weight node
    if inBounds(event.x, event.y, 280, 20, 300, 40): 
        app.movingWeightNodeC = True
        app.customWeight = int(input('Please enter a weight: '))
        if app.movingWeightNodeC:
            app.movingStartingNode = False
            app.movingTargetNode = False
            app.movingWallNode = False

            app.movingWeightNode3 = False
            app.movingWeightNode1 = False
            app.movingWeightNode7 = False


#Doesn't remove the current walling
def refreshForNewVisualize(app):
    app.path = [ ]
    app.bfsSearchQueue = deque()
    app.dfsSearchStack = deque()
    app.dijkstraSearchQueue = deque()
    app.aStarSearchQueue = deque()
    app.visualizedList = [ ]
    app.visualizedIndex = 0
    app.isVisualizing = False
        

def inBoundsOfAlgoButtons(app, event):
    #bfs button
    if inBounds(event.x, event.y, app.width-550, 20, app.width-430, 60):
        refreshForNewVisualize(app)
        graph = createAdjacencyList(initNodeList(app), 1)
        app.path = bfsSearch(app, graph, app.startingNode, app.targetNode)
        if app.path != None:
            app.isVisualizing = True

    #dfs button
    elif inBounds(event.x, event.y, app.width-400, 20, app.width-280, 60):
        refreshForNewVisualize(app)
        graph = createAdjacencyList(initNodeList(app), 1)
        app.path = dfsSearch(app, graph, app.startingNode, app.targetNode)
        if app.path != None:
            app.isVisualizing = True

    #dijkstras button
    elif inBounds(event.x, event.y, app.width-550, 80, app.width-430, 120):
        refreshForNewVisualize(app)
        graph = createWeightedAdjacencyList(app.nodeList, 1)
        app.path = dijkstraSearch(app, graph, app.startingNode, app.targetNode)
        if app.path != None:
            app.isVisualizing = True
        
    #A* button
    elif inBounds(event.x, event.y, app.width-400, 80, app.width-280, 120):
        refreshForNewVisualize(app)
        graph = createWeightedAdjacencyList(app.nodeList, 1)
        app.path = aStar(app, graph, app.startingNode, app.targetNode)
        if app.path != None:
            app.isVisualizing = True
        


def inBoundsOfSpeedButtons(app, event):
    #fast speed
    if inBounds(event.x, event.y, app.width - 250, 20, app.width - 230, 40):
        print('fast')
        app.timerDelay = 0 
        app.fastMode = True
        if app.fastMode:
            app.mediumMode = False
            app.slowMode = False
    #medium speed
    if inBounds(event.x, event.y, app.width - 250, 60, app.width - 230, 80): 
        print('md')
        app.timerDelay = 35 
        app.mediumMode = True
        if app.mediumMode:
            app.fastMode = False
            app.slowMode = False
    #slow speed
    if inBounds(event.x, event.y, app.width - 250, 100, app.width - 230, 120): 
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
    app.dijkstraSearchQueue = deque()
    app.aStarSearchQueue = deque()
    app.visualizedList = [ ]
    app.visualizedIndex = 0
    app.isVisualizing = False
    app.timer = 0
    app.movingWeightNode1 = False
    app.movingWeightNode3 = False
    app.movingWeightNode7 = False
    app.movingWeightNodeC = False

    app.nodeList = initWeightedNodeList(app)

def clearPath(app):
    app.wallNodes = set()
    app.path = [ ]
    app.bfsSearchQueue = deque()
    app.dfsSearchStack = deque()
    app.dijkstraSearchQueue = deque()
    app.aStarSearchQueue = deque()
    app.visualizedList = [ ]
    app.visualizedIndex = 0
    app.isVisualizing = False
    app.nodeList = initWeightedNodeList(app)

        

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

def drawWeightedNodes(app, canvas):
    #1 weight button
    if app.movingWeightNode1:
        weightNode1 = 'light gray'
    else:
        weightNode1 = 'white'
    canvas.create_rectangle(150, 20, 170, 40, fill=weightNode1)
    canvas.create_text(180, 30, text='1 Weight Node', anchor='w')
    #3 weight button
    if app.movingWeightNode3:
        weightNode3 = 'light green'
    else:
        weightNode3 = 'white'
    canvas.create_rectangle(150, 60, 170, 80, fill=weightNode3)
    canvas.create_text(180, 70, text='3 Weight Node', anchor='w')
    #7 weight button
    if app.movingWeightNode7:
        weightNode7 = 'brown'
    else:
        weightNode7 = 'white'           
    canvas.create_rectangle(150, 100, 170, 120, fill=weightNode7)
    canvas.create_text(180, 110, text='7 Weight Node', anchor='w')
    # custom weight button
    if app.movingWeightNodeC:
        if app.customWeight != None:
            if app.customWeight == 1:
                customWeightColor = 'white'
            elif app.customWeight == 3:
                customWeightColor = 'light green'
            elif app.customWeight == 7:
                customWeightColor = 'brown'
            else:
                customWeightColor = intToColor(app.customWeight)
        else:
            customWeightColor = 'white'
    else:
        customWeightColor = 'white'
    canvas.create_rectangle(280, 20, 300, 40, fill=customWeightColor)
    canvas.create_text(310, 30, text='Custom Weight Node', anchor='w')



# def drawCreateMazeButton(app, canvas):
#     pass

def drawAlgorithmButtons(app, canvas):
    #bfs button
    canvas.create_rectangle(app.width-550, 20, app.width-430, 60)
    canvas.create_text(app.width-490, 40, text='BFS')
    #dfs button
    canvas.create_rectangle(app.width-400, 20, app.width-280, 60)
    canvas.create_text(app.width-340, 40, text='DFS')
    #dijkstras button
    canvas.create_rectangle(app.width-550, 80, app.width-430, 120)
    canvas.create_text(app.width-490, 100, text='Dijkstra')
    #A* button
    canvas.create_rectangle(app.width-400, 80, app.width-280, 120)
    canvas.create_text(app.width-340, 100, text='A*')



def drawSpeedButtons(app, canvas):
    #fast speed button
    if app.fastMode:
        fastModeColor = 'black'
    else:
        fastModeColor = 'white'
    canvas.create_rectangle(app.width - 250, 20, app.width - 230, 40, fill=fastModeColor)
    canvas.create_text(app.width - 220, 30, text='Fast', anchor='w')
    #medium speed button
    if app.mediumMode:
        mediumModeColor = 'black'
    else:
        mediumModeColor = 'white'
    canvas.create_rectangle(app.width - 250, 60, app.width - 230, 80, fill=mediumModeColor)
    canvas.create_text(app.width - 220, 70, text='Medium', anchor='w')
    #slow speed button
    if app.slowMode:
        slowModeColor = 'black'
    else:
        slowModeColor = 'white'
    canvas.create_rectangle(app.width - 250, 100, app.width - 230, 120, fill=slowModeColor)
    canvas.create_text(app.width - 220, 110, text='Slow', anchor='w')


def drawResetButtons(app, canvas):
    #reset button
    canvas.create_rectangle(app.width-140, 20, app.width-20, 60)
    canvas.create_text(app.width-80, 40, text='Reset')
    #clear path button
    canvas.create_rectangle(app.width-140, 80, app.width-20, 120)
    canvas.create_text(app.width-80, 100, text='Clear Path')