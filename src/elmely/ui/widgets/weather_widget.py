from __future__ import annotations

from elmely.ui.weather_icons import get_weather_icon

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
)

from elmely.models.weather import Weather
from elmely.ui.widgets.forecast_hour_widget import (
    ForecastHourWidget,
)


class WeatherWidget(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("InfoCard")

        self.setMinimumSize(
            560,
            180,
        )

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

        title_font = QFont(
            "Segoe UI",
            10,
        )

        title_font.setBold(True)

        title.setFont(
            title_font
        )

        main_layout.addWidget(
            title
        )

        #
        # Øverste rad
        #

        top_layout = QHBoxLayout()

        self.icon_label = QLabel("☀")

        icon_font = QFont(
            "Segoe UI",
            28,
        )

        self.icon_label.setFont(
            icon_font
        )

        self.temperature_label = QLabel(
            "--.- °C"
        )

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
            alignment=Qt.AlignTop,
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

            label.setFont(
                info_font
            )

            main_layout.addWidget(
                label
            )

        #
        # 12 timers prognose
        #

        self.forecast_layout = QHBoxLayout()

        self.forecast_layout.setSpacing(4)

        self.forecast_widgets = []

        for _ in range(12):

            widget = ForecastHourWidget()

            self.forecast_widgets.append(
                widget
            )

            self.forecast_layout.addWidget(
                widget
            )

        self.forecast_layout.addStretch()

        main_layout.addSpacing(10)

        main_layout.addLayout(
            self.forecast_layout
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

        self.icon_label.setText(

            get_weather_icon(

                weather.weather_code,

                weather.is_day,

            )

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

        #
        # Prognose
        #

        for widget, forecast in zip(

            self.forecast_widgets,

            weather.forecast,

        ):

            widget.set_forecast(
                forecast
            )