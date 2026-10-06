import math

fingers = {
        "index": [5, 6, 8],
        "middle": [9, 10, 12],
        "ring": [13, 14, 16],
        "little": [17, 18, 20]
    }

def dist(a, b):
    return round(math.dist((a.x, a.y), (b.x, b.y)), 2)

# used Limit from data
def isCurled(hand, mcp, pip, tip):
    mcpTip = dist(hand[mcp], hand[tip])
    mcpPip = dist(hand[mcp], hand[pip])

    return True if mcpTip < (0.8*mcpPip) else False

# Js check if the hand is a fist
def fisted(hand):
    global fingers

    is_curled = 0

    for _, count in fingers.items():
        if isCurled(hand, count[0], count[1], count[2]):
            is_curled += 1  
    
    return True if is_curled >=3 else False


def calcMean(hand):
    global fingers
    meanXls = []
    meanYls = []
    for _, pts in fingers.items():
        meanX = 0
        meanY = 0
        for pt in pts:
            meanX += hand[pt].x
            meanY += hand[pt].y

        meanXls.append(round(meanX/3, 2))
        meanYls.append(round(meanY/3, 2))

    return (round((sum(meanXls) / len(meanXls)), 4), round((sum(meanYls) / len(meanYls)), 4))

def turn(y1Mean,y2Mean, y1, y2):
    dely1 = y1-y1Mean
    dely2 = y2-y2Mean

    if dely1 >=0.12 and dely2 <= -0.12:
        return "RIGHT"

    if dely2 >=0.12 and dely1 <= -0.12:
            return "LEFT"

    