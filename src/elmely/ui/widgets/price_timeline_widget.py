from __future__ import annotations
from tkinter import font

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPainter
from PySide6.QtWidgets import QWidget, QToolTip

from elmely.models.timeline_item import TimelineItem
from elmely.models.timeline_marker import TimelineMarker


class PriceTimelineWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.items: list[TimelineItem] = []

        #
        # Lav tidslinje
        #

        self._hover_index = -1

        self.setMinimumHeight(48)
        self.setMouseTracking(True)

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
                hovered=(index == self._hover_index),
            )

            previous_hour = hour


    def mouseMoveEvent(self, event):

        if not self.items:
            return

        spacing = self.width() / len(self.items)
        index = int(event.position().x() / spacing)

        if index < 0 or index >= len(self.items):
            if self._hover_index != -1:
                self._hover_index = -1
                self.update()
                QToolTip.hideText()
            return

        if index != self._hover_index:
            self._hover_index = index
            self.update()

            QToolTip.showText(
                event.globalPosition().toPoint(),
                self.items[index].tooltip_text(),
                self,
            )

    def leaveEvent(self, event):

        self._hover_index = -1
        self.update()
        QToolTip.hideText()
        super().leaveEvent(event)

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
        hovered: bool = False,
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
                hovered,
            )
    def _draw_circle(
        self,
        painter: QPainter,
        x: int,
        color: QColor,
        hovered: bool = False,
    ):

        painter.setPen(Qt.PenStyle.NoPen)

        painter.setBrush(color)

        size = 12 if hovered else 10

        painter.drawEllipse(
            x - size // 2,
            20 - (size - 10) // 2,
            size,
            size,
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