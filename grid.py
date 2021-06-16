
def getCellBounds(app, row, col):
    gridWidth = app.width - app.margin * 2
    gridHeight = app.height * 3/4
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = col * cellWidth + app.margin
    y0 = row * cellHeight + (app.height // 4 - app.margin)
    x1 = x0 + cellWidth
    y1 = y0 + cellHeight
    return x0, y0, x1, y1

def getCell(app, x, y):
    gridWidth = app.width - app.margin * 2
    gridHeight = app.height * 3/4
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - (app.height // 4 - app.margin)) / cellHeight)
    col = int((x - app.margin) / cellWidth)
    print(x, y)
    print(col, row)
    if row not in range(0, app.rows) or col not in range(0, app.cols):
        return 
    return row, col

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

def drawWallNodes(app, canvas):
    if len(app.wallNodes) <= 0: return
    for row, col in app.wallNodes:
        x0,y0,x1,y1 = getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill='black')