from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from elmely.models.weather import ForecastHour
from elmely.ui.weather_icons import get_weather_icon


class ForecastHourWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedWidth(66)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            4,
            4,
            4,
            4,
        )

        layout.setSpacing(2)

        #
        # Klokkeslett
        #

        self.time_label = QLabel("--")

        self.time_label.setAlignment(
            Qt.AlignCenter
        )

        #
        # Værikon
        #

        self.icon_label = QLabel("?")

        self.icon_label.setAlignment(
            Qt.AlignCenter
        )

        font = self.icon_label.font()

        font.setPointSize(18)

        self.icon_label.setFont(font)

        #
        # Temperatur
        #

        self.temperature_label = QLabel("--°")

        self.temperature_label.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            self.time_label
        )

        layout.addWidget(
            self.icon_label
        )

        layout.addWidget(
            self.temperature_label
        )

    def set_forecast(
        self,
        forecast: ForecastHour,
    ):

        self.time_label.setText(
            forecast.timestamp.strftime("%H")
        )

        self.icon_label.setText(
            get_weather_icon(
                forecast.weather_code,
                True,
            )
        )

        self.temperature_label.setText(
            f"{forecast.temperature:.0f}°"
        )