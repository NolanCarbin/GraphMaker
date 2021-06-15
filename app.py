from cmu_112_graphics import *


def appStarted(app):
    app.rows = 20
    app.cols = 30
    app.gridMargin = app.width // 100

def appStopped(app):
    pass

def mousePressed(app, event):
    pass

def keyPressed(app, event):
    pass

def timerFired(app):
    pass

def redrawAll(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            x0, y0, x1, y1 = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1)

def getCellBounds(app, row, col):
    gridWidth = app.width - app.gridMargin * 2
    gridHeight = app.height * 3/4
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = col * cellWidth + app.gridMargin
    y0 = row * cellHeight + (app.height //4 - app.gridMargin)
    x1 = x0 + cellWidth
    y1 = y0 + cellHeight
    return x0, y0, x1, y1



runApp(width=1000, height=600)