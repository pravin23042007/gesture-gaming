def detect_gesture(landmarks):
    """
    Detect gestures based on body landmarks
    Returns: LEFT, RIGHT, JUMP, IDLE
    """

    if not landmarks:
        return "IDLE"

    left_hand = landmarks[15]
    right_hand = landmarks[16]
    nose = landmarks[0]

    # Jump (both hands up)
    if left_hand.y < nose.y and right_hand.y < nose.y:
        return "JUMP"

    # Move Left
    if left_hand.x < nose.x - 0.2:
        return "LEFT"

    # Move Right
    if right_hand.x > nose.x + 0.2:
        return "RIGHT"

    return "IDLE"