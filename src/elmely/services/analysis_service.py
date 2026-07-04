from __future__ import annotations

from elmely.models.price_period import PricePeriod
from elmely.models.timeline_item import TimelineItem
from elmely.models.timeline_marker import TimelineMarker
from elmely.models.total_price import TotalPrice


class AnalysisService:
    """
    Utfører analyser av strømpriser.
    """

    def find_cheapest_period(
        self,
        prices: list[TotalPrice],
        hours: int,
    ) -> PricePeriod | None:

        if not prices:
            return None

        if hours <= 0:
            raise ValueError("hours must be greater than zero")

        if len(prices) < hours:
            return None

        best_period = None
        lowest_average = float("inf")

        #
        # Glidende vindu
        #

        for start in range(len(prices) - hours + 1):

            window = prices[start:start + hours]

            average = (
                sum(price.total for price in window)
                / hours
            )

            if average < lowest_average:

                lowest_average = average

                best_period = PricePeriod(

                    start=window[0].timestamp,

                    end=window[-1].timestamp,

                    hours=hours,

                    average_price=average,

                )

        return best_period

    #
    # ---------------------------------------------------------
    # Timeline
    # ---------------------------------------------------------
    #

    def create_timeline(
        self,
        prices: list[TotalPrice],
        cheap_limit: float = 0.20,
        expensive_limit: float = 1.50,
    ) -> list[TimelineItem]:

        if not prices:
            return []

        #
        # Finn prisgrenser
        #

        values = sorted(
            price.total
            for price in prices
        )

        low_limit = values[len(values) // 3]

        high_limit = values[(len(values) * 2) // 3]

        items: list[TimelineItem] = []

        for price in prices:

            #
            # Relativ pris
            #

            if price.total <= low_limit:

                relative = 0

            elif price.total >= high_limit:

                relative = 2

            else:

                relative = 1

            #
            # Absolutt markering
            #

            marker = TimelineMarker.NORMAL

            if price.total <= cheap_limit:

                marker = TimelineMarker.CHEAP

            elif price.total >= expensive_limit:

                marker = TimelineMarker.EXPENSIVE

            items.append(

                TimelineItem(

                    timestamp=price.timestamp,

                    total_price=price.total,

                    relative_level=relative,

                    marker=marker,

                )

            )

        return items