from cmu_112_graphics import *


def appStarted(app):
    app.rows = 20
    app.cols = 30
    app.gridMargin = app.width // 100
    app.startingNode = None
    app.targetNode = None
    app.movingStartingNode = False
    app.movingTargetNode = False
    app.movingWallNode = False

def appStopped(app):
    pass

def mousePressed(app, event):
    if app.movingStartingNode:
        app.startingNode = getCell(app, event.x, event.y)  
    elif app.movingTargetNode:
        app.targetNode = getCell(app, event.x, event.y) 
    inBoundsOfButtons(app, event)

def inBounds(x, y, recX0, recY0, recX1, recY1):
    return (recX0 <= x <= recX1 and 
            recY0 <= y <= recY1)
    

def inBoundsOfButtons(app, event):
    # (20, 20, 40, 40) starting node button
    if inBounds(event.x, event.y, 20, 20, 40, 40): 
        app.movingStartingNode = not app.movingStartingNode
    # (20, 60, 40, 80) target node button
    if inBounds(event.x, event.y, 20, 60, 40, 80): 
        app.movingTargetNode = not app.movingTargetNode
    # (20, 100, 40, 120) wall node button
    if inBounds(event.x, event.y, 20, 100, 40, 120): 
        app.movingWallNode = not app.movingWallNode
    

def keyPressed(app, event):
    pass

def timerFired(app):
    pass

def getCellBounds(app, row, col):
    gridWidth = app.width - app.gridMargin * 2
    gridHeight = app.height * 3/4
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = col * cellWidth + app.gridMargin
    y0 = row * cellHeight + (app.height // 4 - app.gridMargin)
    x1 = x0 + cellWidth
    y1 = y0 + cellHeight
    return x0, y0, x1, y1

def getCell(app, x, y):
    gridWidth = app.width - app.gridMargin * 2
    gridHeight = app.height * 3/4
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - (app.height // 4 - app.gridMargin)) / cellHeight)
    col = int((x - app.gridMargin) / cellWidth)
    if row not in range(0, app.rows) or col not in range(0, app.cols):
        return None
    return row, col

def redrawAll(app, canvas):
    drawGrid(app, canvas)
    drawStartingNode(app, canvas)
    drawTargetNode(app, canvas)
    drawButtons(app, canvas)

def drawGrid(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            x0, y0, x1, y1 = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1)

def drawStartingNode(app, canvas):
    if app.startingNode == None: return
    startingRow, startingCol = app.startingNode
    x0,y0,x1,y1 = getCellBounds(app, startingRow, startingCol)
    canvas.create_oval(x0,y0,x1,y1,fill='blue')

def drawTargetNode(app, canvas):
    if app.targetNode == None: return
    targetRow, targetCol = app.targetNode
    x0,y0,x1,y1 = getCellBounds(app, targetRow, targetCol)
    canvas.create_oval(x0,y0,x1,y1,fill='green')

def drawButtons(app, canvas):
    canvas.create_rectangle(20, 20, 40, 40)
    # canvas.create_text()
    canvas.create_rectangle(20, 60, 40, 80)
    # canvas.create_text()
    canvas.create_rectangle(20, 100, 40, 120)
    # canvas.create_text()


runApp(width=1000, height=600)