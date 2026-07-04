from __future__ import annotations

from enum import IntEnum


class TimelineMarker(IntEnum):
    """
    Markeringssymbol for en time i prisprognosen.
    """

    NORMAL = 0
    CHEAP = 1
    EXPENSIVE = 2