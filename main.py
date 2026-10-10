from hands import see_hands
from process import fisted, calcMean, turn, shoot
import keyboard 
import time

def main():
    print("MAIN STARTED")
    stabilityCount = 0
    baselineSet = False # Bool added here so that if the cam loses control for a sec it doesnt once again assign new mean baseline values 

    for hands in see_hands():
        if len(hands) >= 2:
            if stabilityCount > 30:
                
                x1, y1 = calcMean(hands[0])
                x2, y2 = calcMean(hands[1])
                whereGo = turn(y1Mean, y2Mean, y1, y2)
                doShoot = shoot(hands)

                if doShoot:
                    if doShoot == "SHOOT":
                        keyboard.send("space")
                    else:
                        keyboard.release("w")
                        print("W out")
                        keyboard.press("s")
                        print("S in")
                else:
                    keyboard.press("w")
                if whereGo:
                    if whereGo == "RIGHT":
                        keyboard.press("d")
                        keyboard.release("a")
                        time.sleep(0.2)
                        keyboard.release("d")
                    else:
                        keyboard.press("a")
                        keyboard.release("d")
                        time.sleep(0.2)
                        keyboard.release("a")

                else:
                    keyboard.release("a")
                    keyboard.release("d")
                    keyboard.release("s")
            elif fisted(hands[0]) and fisted(hands[-1]):
                stabilityCount += 1
                print("BOTH HANDS ARE FISTS")
                print(
                    "LEFT/RIGHT:",
                    fisted(hands[0]),
                    fisted(hands[-1])
                )
                if stabilityCount == 30 and not baselineSet:
                    print("FULLY STABLE")
                    print("------------------------")
                    print("------------------------")
                    print("------------------------")
                    x1Mean, y1Mean = calcMean(hands[0])
                    x2Mean, y2Mean = calcMean(hands[1])
                    baselineSet = True
                    keyboard.press("w")
        else:
            print("Need two hands")        

if __name__ == "__main__":
    main()

