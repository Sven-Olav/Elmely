from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Price:

    start: datetime

    end: datetime

    spot_price_dkk: float