from collections import defaultdict

strike = "X"
spare = "/"
gutter = "-"
frames_idx = {
    1: [0, 1],
    2: [2, 3],
    3: [4, 5],
    4: [6, 7],
    5: [8, 9],
    6: [10, 11],
    7: [12, 13],
    8: [14, 15],
    9: [16, 17],
    10: [18, 19, 20],
}


def spare_score(frames, frame):
    # Spare you only include the next ball
    spare_idx = frames_idx[frame + 1][0]
    score = frames[spare_idx]
    if score == strike:
        return 10
    elif score == gutter:
        return 0
    else:
        return int(score)


def strike_score(frames, frame):
    # On a Strike you include the next 2 balls
    first_ball, second_ball = 0, 0
    first_strike_idx = frames_idx[frame + 1][0]
    first_ball_score = frames[first_strike_idx]

    # Get first ball score and prepare second ball index
    if first_ball_score == strike:
        first_ball = 10
        if frame == 9:
            second_strike_idx = frames_idx[frame + 1][1]
        else:
            second_strike_idx = frames_idx[frame + 2][0]
    else:
        second_strike_idx = frames_idx[frame + 1][1]
        first_ball = int(first_ball_score) if first_ball_score.isdigit() else 0

    # Get second ball score
    second_ball_score = frames[second_strike_idx]
    if second_ball_score == strike or second_ball_score == spare:
        second_ball = 10
        if first_ball < 10:
            first_ball = 0
    elif second_ball_score.isdigit():
        second_ball = int(second_ball_score)

    return first_ball + second_ball


def frame_ten_score(frames, frame):
    # Start by getting the score for each bowl:
    final_frame_score = 0
    last_ball_score = 0
    frame_score = frames[frames_idx[frame][0] : frames_idx[frame][-1] + 1]
    for idx, score in enumerate(frame_score):
        if score == strike:
            final_frame_score += 10
        elif score == spare and idx == 1:
            final_frame_score = 10
        elif score == spare and idx == 2:
            if final_frame_score % 10:
                final_frame_score += 10 - final_frame_score % 10
            else:
                final_frame_score += 10
        elif score == gutter:
            continue
        elif score.isdigit():
            final_frame_score = final_frame_score + int(score)
    return final_frame_score


def not_special(frame_score):
    if frame_score[0].isdigit() and frame_score[1].isdigit():
        return int(frame_score[0]) + int(frame_score[1])
    elif frame_score[0].isdigit():
        return int(frame_score[0])
    elif frame_score[1].isdigit():
        return int(frame_score[1])
    else:
        return 0


def calculate_score(frames: str) -> int:
    """Calculates a total 10-pin bowling score from a string of frame data."""
    # Frame number: Frame Score Positions
    score = 0

    for f, idx in frames_idx.items():
        # Frame 10 is the exception we need to handle
        if f == 10:
            score = score + frame_ten_score(frames, f)
            print(score)
            continue
        # All other frames
        frame_score = frames[idx[0] : idx[-1] + 1]
        if frame_score[0] == strike:
            score = score + 10 + strike_score(frames, f)
        elif frame_score[1] == spare:
            score = score + 10 + spare_score(frames, f)
        else:
            score = score + not_special(frame_score)
        print(score)

    return score


# calculate_score("36546/819/7--/717/3/-")
# calculate_score("X X X X X X X X X XXX")
