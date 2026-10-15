import time
import keyboard
from hands import see_hands
from process import fisted, calcMean, turn, change

lastPressedRestart = 0
lastPressedRepeat = 0
cooldown = 2

def checkTurn(command):
    global lastPressedRepeat, lastPressedRestart, cooldown
    if command == "BACK":
        # keyboard.release("w")
        # keyboard.press("s")
        print("STOOOOOP")
    elif command == "RESTART":
        now = time.monotonic()
        if now - lastPressedRestart > cooldown:
            lastPressedRestart = now
            print("RESTARTTTT")
            # keyboard.send("t")
    elif command == "REPEAT":
        nowRepeat = time.monotonic()
        if nowRepeat - lastPressedRepeat > cooldown:
            lastPressedRepeat = nowRepeat
            print("REPEASRTTTT")
            # keyboard.send("r")
    else:
        # keyboard.release("s")
        # keyboard.press("w")
        print("forWARDDDDD")


def main():
    print("MAIN STARTED - FIXED LOOP")
    stabilityCount = 0
    baselineSet = False
    
    y1Mean, y2Mean = 0, 0
    current_key = None  # Tracks what's currently held down to prevent spamming

    for hands in see_hands():
        if len(hands) >= 2:
            if baselineSet:
                ___, y1 = calcMean(hands[0])
                __, y2 = calcMean(hands[1])
                whereGo = turn(y1Mean, y2Mean, y1, y2)
                doShoot = change(hands)

                if doShoot:
                    checkTurn(doShoot)
                elif whereGo == "RIGHT":
                    pass
                elif whereGo == "LEFT":
                    pass
                else:
                    pass

            elif fisted(hands[0]) and fisted(hands[-1]):
                stabilityCount += 1
                print(f"Holding fists... {stabilityCount}/30")
                if stabilityCount >= 30 and not baselineSet:
                    x1Mean, y1Mean = calcMean(hands[0])
                    x2Mean, y2Mean = calcMean(hands[1])
                    baselineSet = True
                    keyboard.press("w")
                    print("BASELINE LOCKED. RUNNING.")
        else:
            print("Looking for two hands...")

if __name__ == "__main__":
    main()