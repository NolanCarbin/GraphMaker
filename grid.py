from intToColor import intToColor

def getCellBounds(app, row, col):
    gridWidth = app.width - app.xMargin * 2
    gridHeight = app.height - (app.yMarginTop + app.yMarginBottom)
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = col * cellWidth + app.xMargin
    y0 = row * cellHeight + app.yMarginTop
    x1 = x0 + cellWidth
    y1 = y0 + cellHeight
    return x0, y0, x1, y1

def getCell(app, x, y):
    if not insideGrid(app, x, y): return None
    gridWidth = app.width - app.xMargin * 2
    gridHeight = app.height - (app.yMarginTop + app.yMarginBottom)
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - app.yMarginTop) / cellHeight)
    col = int((x - app.xMargin) / cellWidth)
    return row, col

def insideGrid(app, x, y):
    return (app.xMargin <= x <= app.width - app.xMargin and 
            app.yMarginTop <= y <= app.height - app.yMarginBottom)

# def drawGrid(app, canvas):
#     for row in range(app.rows):
#         for col in range(app.cols):
#             x0, y0, x1, y1 = getCellBounds(app, row, col)
#             canvas.create_rectangle(x0, y0, x1, y1)

def drawGrid(app, canvas):
    for row, col, weight in app.nodeList:
        if weight == 1:
            color = 'white'
        elif weight == 3:
            color = 'light green'
        elif weight == 7:
            color = 'brown'
        else:
            color = intToColor(weight)
        x0,y0,x1,y1 = getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill=color)

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

def drawWallNodes(app, canvas):
    if len(app.wallNodes) <= 0: return
    for row, col in app.wallNodes:
        x0,y0,x1,y1 = getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill='black')









