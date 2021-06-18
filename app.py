from cmu_112_graphics import *
from collections import deque
from visualizer import *
from grid import *
from buttons import *


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
    app.path = []

    app.fastMode = False
    app.mediumMode = True
    app.slowMode = False

    app.bfsSearchQueue = deque()
    app.dfsSearchStack = deque()
    app.visualizedList = [ ]
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
    selectedNode = getCell(app, event.x, event.y)
    #toggles moving flag for the nodes if clicked on
    if selectedNode == app.startingNode: 
        app.movingStartingNode = True
        app.movingTargetNode = False
        app.movingWallNode = False
    elif selectedNode == app.targetNode: 
        app.movingTargetNode = True
        app.movingStartingNode = False
        app.movingWallNode = False

    #logic that moves the nodes
    if selectedNode != None:
        if app.movingStartingNode:
            if selectedNode in app.wallNodes:
                app.wallNodes.remove(selectedNode)
            app.startingNode = selectedNode 
            refreshForNewSearch(app)
        elif app.movingTargetNode:
            if selectedNode in app.wallNodes:
                app.wallNodes.remove(selectedNode)
            app.targetNode = selectedNode
            refreshForNewSearch(app)
        elif app.movingWallNode:
            if selectedNode in app.wallNodes:
                app.wallNodes.remove(selectedNode)
            elif selectedNode == app.startingNode or selectedNode == app.targetNode:
                return
            else:
                app.wallNodes.add((selectedNode))
                refreshForNewSearch(app)

def keyPressed(app, event):
    pass

def timerFired(app):
    # app.timer += 1
    bfsVisualizer(app)
    dfsVisualizer(app) 

# def isOneSecond(app):
#     return app.timer % 10 == 0


def redrawAll(app, canvas):
    drawGrid(app, canvas)
    drawvisualizedList(app, canvas)
    if not app.isVisualizing:
        drawPath(app, canvas)
    drawStartingNode(app, canvas)
    drawTargetNode(app, canvas)
    drawWallNodes(app, canvas)
    drawNodeButtons(app, canvas)
    drawAlgorithmButtons(app, canvas)
    drawResetButtons(app, canvas)
    drawSpeedButtons(app, canvas)

runApp(width=1000, height=600)