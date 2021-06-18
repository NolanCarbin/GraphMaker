from grid import getCellBounds

def bfsVisualizer(app):
    if app.path != None:
        if len(app.bfsSearchQueue) >= 1:
            if app.visualizedIndex < len(app.bfsSearchQueue) - 1:
                app.visualizedIndex += 1
                app.visualizedList.append(app.bfsSearchQueue[app.visualizedIndex])
            else:
                app.isVisualizing = False

def dfsVisualizer(app):
    if app.path != None:
        if len(app.dfsSearchStack) >= 1:
            if app.visualizedIndex < len(app.dfsSearchStack) - 1:
                app.visualizedIndex += 1
                app.visualizedList.append(app.dfsSearchStack[app.visualizedIndex])
            else:
                app.isVisualizing = False

def drawvisualizedList(app, canvas):
    if len(app.visualizedList) >= 1:
        for row, col in app.visualizedList:
            x0,y0,x1,y1 = getCellBounds(app, row, col)
            canvas.create_rectangle(x0,y0,x1,y1,fill='light blue')

def drawPath(app, canvas):
    if app.path == None: return
    for row, col in app.path:
        x0,y0,x1,y1 = getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1,fill='yellow')