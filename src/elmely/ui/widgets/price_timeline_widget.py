from __future__ import annotations
from tkinter import font

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPainter
from PySide6.QtWidgets import QWidget

from elmely.models.timeline_item import TimelineItem
from elmely.models.timeline_marker import TimelineMarker


class PriceTimelineWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.items: list[TimelineItem] = []

        #
        # Lav tidslinje
        #

        self.setMinimumHeight(48)

    def set_items(
        self,
        items: list[TimelineItem],
    ):

        self.items = items

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        if not self.items:
            return

        width = self.width()

        count = len(self.items)

        spacing = width / count

        previous_hour = None

        for index, item in enumerate(self.items):

            hour = item.timestamp.hour

            x = spacing * index + spacing / 2

            #
            # Døgnskille
            #

            if previous_hour == 23 and hour == 0:

                painter.setPen(
                    QColor(190, 190, 190)
                )

                painter.drawLine(
                    int(x - spacing / 2),
                    2,
                    int(x - spacing / 2),
                    self.height() - 2,
                )

            #
            # Klokkeslett
            #

            painter.setPen(
                QColor(70, 70, 70)
            )

            font = painter.font()

            font.setPointSize(8)

            painter.setFont(font)

            painter.drawText(
                int(x - 12),
                2,
                24,
                16,
                Qt.AlignmentFlag.AlignCenter,
                f"{hour:02d}",
            )

            #
            # Marker
            #

            self._draw_symbol(
                painter,
                int(x),
                item,
            )

            previous_hour = hour

    #
    # --------------------------------------------------
    # Private metoder
    # --------------------------------------------------
    #

    def _marker_color(
        self,
        level: int,
    ) -> QColor:

        if level == 0:

            return QColor(
                35,
                180,
                75,
            )

        if level == 1:

            return QColor(
                235,
                185,
                40,
            )

        return QColor(
            220,
            60,
            60,
        )

    def _draw_symbol(
        self,
        painter: QPainter,
        x: int,
        item: TimelineItem,
    ):

        color = self._marker_color(
            item.relative_level
        )

        if item.marker == TimelineMarker.CHEAP:

            self._draw_star(
                painter,
                x,
                color,
            )

        elif item.marker == TimelineMarker.EXPENSIVE:

            self._draw_exclamation(
                painter,
                x,
                color,
            )

        else:

            self._draw_circle(
                painter,
                x,
                color,
            )
    def _draw_circle(
        self,
        painter: QPainter,
        x: int,
        color: QColor,
    ):

        painter.setPen(Qt.PenStyle.NoPen)

        painter.setBrush(color)

        painter.drawEllipse(
            x - 5,
            20,
            10,
            10,
    )

    def _draw_star(
        self,
        painter: QPainter,
        x: int,
        color: QColor,
    ):

        painter.setPen(color)

        font = QFont()

        font.setPointSize(11)

        font.setBold(True)

        painter.setFont(font)

        painter.drawText(
            x - 7,
            30,
            "★",
        )

    def _draw_exclamation(
        self,
        painter: QPainter,
        x: int,
        color: QColor,
    ):

        painter.setPen(color)

        font = QFont()

        font.setPointSize(11)

        font.setBold(True)

        painter.setFont(font)

        painter.drawText(
            x - 3,
            30,
            "!",
        )