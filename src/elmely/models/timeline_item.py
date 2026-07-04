from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from elmely.models.timeline_marker import TimelineMarker


@dataclass(slots=True)
class TimelineItem:
    """
    Ett element i prisprognosen.
    """

    #
    # Starttidspunkt for timen
    #

    timestamp: datetime

    #
    # Totalpris for timen (DKK/kWh)
    #

    total_price: float = 0.0

    #
    # Relativ pris:
    #
    # 0 = grønn
    # 1 = gul
    # 2 = rød
    #

    relative_level: int = 1

    #
    # Symbol som skal vises
    #

    marker: TimelineMarker = TimelineMarker.NORMAL