from datetime import timedelta
from datetime import datetime
from typing import List


def get_srt_section_ids(text: str) -> List[int]:
    sections = text.strip().split("\n\n")
    timings = []
    for piece in sections:
        piece_id, piece_time, piece_text = piece.split("\n")
        start_time, end_time = piece_time.split(" --> ")
        total_time = (
            datetime.strptime(end_time.split(",")[0], "%H:%M:%S")
            - datetime.strptime(start_time.split(",")[0], "%H:%M:%S")
        ).total_seconds()
        piece_length = len(piece_text)
        timings.append((total_time / piece_length, int(piece_id)))
    return [tup[1] for tup in sorted(timings)]
