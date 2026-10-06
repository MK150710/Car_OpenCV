from hands import see_hands
from process import fisted, calcMean, turn

def main():

    print("MAIN STARTED")
    stabilityCount = 0
    baselineSet = False # Bool added here so that if the cam loses control for a sec it doesnt once again assign new mean baseline values 

    for hands in see_hands():
        if len(hands) >= 2:
            if stabilityCount > 30:
                
                x1, y1 = calcMean(hands[0])
                x2, y2 = calcMean(hands[1])
                print(turn(y1Mean, y2Mean, y1, y2))

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
        else:
            print("Need two hands")        

if __name__ == "__main__":
    main()