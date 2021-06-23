from cmu_112_graphics import *
from collections import deque
from visualizer import *
from grid import *
from buttons import *
import string


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
    app.dijkstraSearchQueue = deque()
    app.aStarSearchQueue = deque()
    app.visualizedList = [ ]
    app.visualizedIndex = 0
    app.isVisualizing = False

    app.nodeList = initWeightedNodeList(app)

    app.movingWeightNode1 = False
    app.movingWeightNode3 = False
    app.movingWeightNode7 = False
    app.movingWeightNodeC = False
    
    app.customWeight = 1
    app.customWeightMessage = None
    app.changingCustomWeight = False
    app.userInputWeight = ''

def appStopped(app):
    pass

def mousePressed(app, event):
    inBoundsOfResetButtons(app, event)
    inBoundsOfSpeedButtons(app, event)
    if not app.isVisualizing and not app.changingCustomWeight:
        moveNodes(app, event)
        inBoundsOfNodeButtons(app, event)
        inBoundsOfWeightButtons(app, event)
        inBoundsOfAlgoButtons(app, event)

        
def moveNodes(app, event):
    selectedNode = getCell(app, event.x, event.y)
    #toggles moving flag for the nodes if clicked on
    if selectedNode == app.startingNode: 
        app.movingStartingNode = True
        app.movingTargetNode = False
        app.movingWallNode = False

        app.movingWeightNode1 = False
        app.movingWeightNode3 = False
        app.movingWeightNode7 = False
        app.movingWeightNodeC = False

    elif selectedNode == app.targetNode: 
        app.movingTargetNode = True
        app.movingStartingNode = False
        app.movingWallNode = False

        app.movingWeightNode1 = False
        app.movingWeightNode3 = False
        app.movingWeightNode7 = False
        app.movingWeightNodeC = False

    #logic that moves the nodes
    if selectedNode != None:
        if app.movingStartingNode:
            if selectedNode in app.wallNodes:
                app.wallNodes.remove(selectedNode)
            app.startingNode = selectedNode 
            refreshForNewVisualize(app)
        elif app.movingTargetNode:
            if selectedNode in app.wallNodes:
                app.wallNodes.remove(selectedNode)
            app.targetNode = selectedNode
            refreshForNewVisualize(app)
        elif app.movingWallNode:
            if selectedNode in app.wallNodes:
                app.wallNodes.remove(selectedNode)
                #add to app.nodeList
                row, col = selectedNode
                app.nodeList.append((row, col, 1))
                app.nodeList.sort()
            elif selectedNode == app.startingNode or selectedNode == app.targetNode:
                return
            else:
                app.wallNodes.add((selectedNode))
                #remove from app.nodeList
                for row, col, weight in app.nodeList:
                    if (row, col) == selectedNode:
                        app.nodeList.remove((row,col,weight))      
                refreshForNewVisualize(app)

        elif app.movingWeightNode1:
            for row, col, weight in app.nodeList:
                if (row, col) == selectedNode:
                    index = app.nodeList.index((row,col,weight))
                    app.nodeList[index] = (row, col, 1)
        elif app.movingWeightNode3:
            for row, col, weight in app.nodeList:
                if (row, col) == selectedNode:
                    index = app.nodeList.index((row,col,weight))
                    app.nodeList[index] = (row, col, 3)
        elif app.movingWeightNode7:
            for row, col, weight in app.nodeList:
                if (row, col) == selectedNode:
                    index = app.nodeList.index((row,col,weight))
                    app.nodeList[index] = (row, col, 7)
        elif app.movingWeightNodeC:
            for row, col, weight in app.nodeList:
                if (row, col) == selectedNode:
                    index = app.nodeList.index((row,col,weight))
                    app.nodeList[index] = (row, col, app.customWeight)


def keyPressed(app, event):
    if app.changingCustomWeight:
        if event.key in string.digits:
            app.userInputWeight += event.key
            app.customWeightMessage = app.userInputWeight
        elif event.key == 'Enter' and app.userInputWeight != '':
            updateCustomWeight(app)
        else:
            app.customWeightMessage = 'Please enter a valid weight'
            app.userInputWeight = ''
        
def updateCustomWeight(app):
    app.customWeight = int(app.userInputWeight)
    app.changingCustomWeight = False
    app.customWeightMessage = None
    app.userInputWeight = ''


def timerFired(app):
    bfsVisualizer(app)
    dfsVisualizer(app) 
    dijkstraVisualizer(app)
    aStarVisualizer(app)

def redrawAll(app, canvas):
    drawGrid(app, canvas)
    drawVisualizedList(app, canvas)
    if not app.isVisualizing:
        drawPath(app, canvas)
    drawStartingNode(app, canvas)
    drawTargetNode(app, canvas)
    drawWallNodes(app, canvas)
    drawNodeButtons(app, canvas)
    drawWeightedNodes(app, canvas)
    drawAlgorithmButtons(app, canvas)
    drawResetButtons(app, canvas)
    drawSpeedButtons(app, canvas)
    drawCustomWeightMessage(app, canvas)

runApp(width=1000, height=600)