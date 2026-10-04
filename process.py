import math

def dist(a, b):
    return round(math.dist((a.x, a.y), (b.x, b.y)), 2)

# used Limit from data
def isCurled(hand, mcp, pip, tip):
    mcpTip = dist(hand[mcp], hand[tip])
    mcpPip = dist(hand[mcp], hand[pip])

    return True if mcpTip < (0.8*mcpPip) else False

# Js check if the hand is a fist
def fisted(hand):
    fingers = {
        "index": [5, 6, 8],
        "middle": [9, 10, 12],
        "ring": [13, 14, 16],
        "little": [17, 18, 20]
    }

    is_curled = 0

    for finger, count in fingers.items():
        if isCurled(hand, count[0], count[1], count[2]):
            is_curled += 1  
    
    

    return True if is_curled >=3 else False