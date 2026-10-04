LANDMARK_NAMES = [
    "Wrist",
    "Thumb CMC",
    "Thumb MCP",
    "Thumb IP",
    "Thumb Tip",
    "Index MCP",
    "Index PIP",
    "Index DIP",
    "Index Tip",
    "Middle MCP",
    "Middle PIP",
    "Middle DIP",
    "Middle Tip",
    "Ring MCP",
    "Ring PIP",
    "Ring DIP",
    "Ring Tip",
    "Pinky MCP",
    "Pinky PIP",
    "Pinky DIP",
    "Pinky Tip"
]


def print_hands(result):

    for hand_num, hand in enumerate(result, 1):

        print(f"\n========== HAND {hand_num} ==========")

        for i, landmark in enumerate(hand):
            print(
                f"{i:2} | "
                f"{LANDMARK_NAMES[i]:12} | "
                f"x: {landmark.x:.4f} | "
                f"y: {landmark.y:.4f}"
            )

        print("================================")