from pathlib import Path
import sys
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from PySide6.QtWidgets import QApplication

from elmely.models.timeline_item import TimelineItem
from elmely.ui.widgets.price_timeline_widget import PriceTimelineWidget
from elmely.models.timeline_marker import TimelineMarker

def main():

    app = QApplication(sys.argv)

    widget = PriceTimelineWidget()

    widget.setWindowTitle("Price Timeline Test")

    widget.resize(900, 48)

    #
    # Starter kl. 18 og viser 13 timer
    #

    start = datetime(2026, 7, 4, 18)

    items = []

    for i in range(13):

        item = TimelineItem(
            timestamp=start + timedelta(hours=i)
        )

        #
        # TEST:
        # 0 = grønn
        # 1 = gul
        # 2 = rød
        #

        item.relative_level = i % 3

        items.append(item)

    widget.set_items(items)

    widget.show()

    app.exec()


if __name__ == "__main__":
    main()

if i % 3 == 0:
    item.marker = TimelineMarker.CHEAP

elif i % 3 == 2:
    item.marker = TimelineMarker.EXPENSIVE