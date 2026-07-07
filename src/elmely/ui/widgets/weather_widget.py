from __future__ import annotations

from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
)

from elmely.models.weather import Weather


class WeatherWidget(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("InfoCard")

        #
        # Litt bredere enn InfoCard siden prognosen skal inn
        # senere.
        #

        self.setMinimumSize(560, 180)

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        main_layout.setSpacing(10)

        #
        # Overskrift
        #

        title = QLabel("Vær")

        title_font = QFont("Segoe UI", 10)
        title_font.setBold(True)

        title.setFont(title_font)

        main_layout.addWidget(title)

        #
        # Øverste rad
        #

        top_layout = QHBoxLayout()

        self.icon_label = QLabel("☀")

        icon_font = QFont("Segoe UI", 28)

        self.icon_label.setFont(icon_font)

        self.temperature_label = QLabel("--.- °C")

        temperature_font = QFont(
            "Segoe UI",
            24,
        )

        temperature_font.setBold(True)

        self.temperature_label.setFont(
            temperature_font
        )

        top_layout.addWidget(
            self.icon_label
        )

        top_layout.addWidget(
            self.temperature_label
        )

        top_layout.addStretch()

        self.updated_label = QLabel(
            "Oppdatert: --"
        )

        updated_font = QFont(
            "Segoe UI",
            8,
        )

        self.updated_label.setFont(
            updated_font
        )

        top_layout.addWidget(
            self.updated_label,
            alignment=Qt.AlignmentFlag.AlignTop,
        )

        main_layout.addLayout(
            top_layout
        )

        #
        # Informasjon
        #

        self.wind_label = QLabel(
            "Vind: --"
        )

        self.uv_label = QLabel(
            "UV: --"
        )

        self.rain_label = QLabel(
            "Regn: --"
        )

        info_font = QFont(
            "Segoe UI",
            10,
        )

        for label in (
            self.wind_label,
            self.uv_label,
            self.rain_label,
        ):

            label.setFont(info_font)

            main_layout.addWidget(label)

        #
        # Prognose
        #

        self.forecast_label = QLabel(
            "12-timers prognose kommer i neste steg..."
        )

        forecast_font = QFont(
            "Segoe UI",
            9,
        )

        self.forecast_label.setFont(
            forecast_font
        )

        self.forecast_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        main_layout.addStretch()

        main_layout.addWidget(
            self.forecast_label
        )

    def set_weather(
        self,
        weather: Weather,
    ):

        self.temperature_label.setText(
            f"{weather.temperature:.1f} °C"
        )

        self.wind_label.setText(
            f"Vind: {weather.wind_speed:.1f} m/s"
        )

        self.uv_label.setText(
            f"UV: {weather.uv_index:.1f}"
        )

        self.rain_label.setText(
            f"Regn: {weather.precipitation_probability:d} %"
        )

        #
        # Foreløpig bruker vi tekst.
        # SVG-ikoner kommer i M018C/D.
        #

        self.icon_label.setText(
            str(weather.weather_code)
        )

        if weather.updated_at is not None:

            self.updated_label.setText(

                "Oppdatert: "

                + weather.updated_at.strftime(
                    "%H:%M"
                )

            )

        else:

            self.updated_label.setText(
                "Oppdatert: --"
            )