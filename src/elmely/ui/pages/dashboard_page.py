from datetime import datetime

from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QWidget

from elmely.core.logger import log

from elmely.services.analysis_service import AnalysisService
from elmely.services.electricity_price_service import ElectricityPriceService
from elmely.services.exchange_rate_service import ExchangeRateService
from elmely.services.scheduler_service import SchedulerService
from elmely.services.tariff_service import TariffService
from elmely.services.weather_service import WeatherService

from elmely.ui.widgets.info_card import InfoCard
from elmely.ui.widgets.price_timeline_widget import PriceTimelineWidget
from elmely.ui.widgets.weather_widget import WeatherWidget


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        self.price_service = ElectricityPriceService()
        self.tariff_service = TariffService()
        self.exchange_service = ExchangeRateService()
        self.analysis_service = AnalysisService()
        self.weather_service = WeatherService()

        page_layout = QVBoxLayout(self)

        page_layout.setContentsMargins(
            30,
            30,
            30,
            30,
        )

        page_layout.setSpacing(18)

        cards = QGridLayout()

        cards.setHorizontalSpacing(25)
        cards.setVerticalSpacing(25)

        self.total_card = InfoCard(
            "Strømpris",
            "--,-- DKK",
            "inkl. avgifter",
        )

        self.currency_card = InfoCard(
            "Valutakurs",
            "--,--",
            "100 DKK",
        )

        self.weather_widget = WeatherWidget()

        cards.addWidget(
            self.total_card,
            0,
            0,
        )

        cards.addWidget(
            self.currency_card,
            0,
            1,
        )

        cards.addWidget(
            self.weather_widget,
            1,
            0,
            1,
            2,
        )

        page_layout.addLayout(cards)

        self.timeline = PriceTimelineWidget()

        page_layout.addWidget(
            self.timeline
        )

        #
        # Scheduler
        #

        self.scheduler = SchedulerService()

        self.scheduler.start(
            self.update_dashboard
        )

    def update_dashboard(self) -> bool:

        #
        # Strøm
        #

        try:

            self.price_service.refresh()

            current_price = (
                self.price_service.get_current_price()
            )

            if current_price is not None:

                total_price = (
                    self.tariff_service.calculate_total_price(
                        current_price
                    )
                )

                self.total_card.set_value(
                    f"{total_price.total:.2f} DKK"
                )

                self.total_card.set_updated(
                    f"Oppdatert: {datetime.now():%H:%M}"
                )

                prices = (
                    self.price_service.get_all_prices()
                )

                if prices:

                    total_prices = [

                        self.tariff_service.calculate_total_price(
                            price
                        )

                        for price in prices

                    ]

                    items = (
                        self.analysis_service.create_timeline(
                            total_prices
                        )
                    )

                    self.timeline.set_items(
                        items
                    )

            else:

                log.warning(
                    "No electricity prices available"
                )

        except Exception:

            log.exception(
                "Failed to update electricity prices"
            )

        #
        # Valutakurs
        #

        try:

            self.exchange_service.refresh()

            rate = self.exchange_service.get_rate()

            display_rate = (
                rate.rate * 100
            )

            self.currency_card.set_value(
                f"{display_rate:.2f} NOK"
            )

            self.currency_card.set_updated(
                "100 DKK"
            )

        except Exception:

            log.exception(
                "Failed to update exchange rate"
            )

        #
        # Vær
        #

        try:

            self.weather_service.refresh()

            weather = (
                self.weather_service.get_weather()
            )

            self.weather_widget.set_weather(
                weather
            )

        except Exception:

            log.exception(
                "Failed to update weather"
            )

        return True