from hands import see_hands
from process import fisted


def main():
    for hands in see_hands():
        if len(hands) >= 2:
            print(
                "LEFT/RIGHT:",
                fisted(hands[0]),
                fisted(hands[-1])
            )
            if fisted(hands[0]) and fisted(hands[-1]):
                
                print("BOTH HANDS ARE FISTS")
        else:
            print("Need two hands")


if __name__ == "__main__":
    main()