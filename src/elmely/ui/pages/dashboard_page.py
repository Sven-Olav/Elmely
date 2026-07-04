from datetime import datetime

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QWidget

from elmely.services.analysis_service import AnalysisService
from elmely.services.electricity_price_service import ElectricityPriceService
from elmely.services.exchange_rate_service import ExchangeRateService
from elmely.services.tariff_service import TariffService

from elmely.ui.widgets.info_card import InfoCard
from elmely.ui.widgets.price_timeline_widget import PriceTimelineWidget


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.price_service = ElectricityPriceService()
        self.tariff_service = TariffService()
        self.exchange_service = ExchangeRateService()
        self.analysis_service = AnalysisService()

        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(30, 30, 30, 30)
        page_layout.setSpacing(18)

        cards = QGridLayout()
        cards.setHorizontalSpacing(25)
        cards.setVerticalSpacing(25)

        self.spot_card = InfoCard("Spotpris", "--,-- DKK", "Oppdatert")
        self.total_card = InfoCard("Totalpris", "--,-- DKK", "inkl. avgifter")
        self.currency_card = InfoCard("Valutakurs", "--,--", "DKK → NOK")
        self.weather_card = InfoCard("Vær", "-- °C", "Bornholm")

        cards.addWidget(self.spot_card, 0, 0)
        cards.addWidget(self.total_card, 0, 1)
        cards.addWidget(self.currency_card, 1, 0)
        cards.addWidget(self.weather_card, 1, 1)

        page_layout.addLayout(cards)

        self.timeline = PriceTimelineWidget()
        page_layout.addWidget(self.timeline)

        self.update_dashboard()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_dashboard)
        self.timer.start(5 * 60 * 1000)

    def update_dashboard(self):

        self.price_service.refresh()

        current_price = self.price_service.get_current_price()
        if current_price is None:
            return

        self.spot_card.set_value(f"{current_price.spot_price_dkk:.3f} DKK")
        self.spot_card.set_updated(f"Oppdatert: {datetime.now():%H:%M}")

        total_price = self.tariff_service.calculate_total_price(current_price)
        self.total_card.set_value(f"{total_price.total:.3f} DKK")
        self.total_card.set_updated(f"Oppdatert: {datetime.now():%H:%M}")

        rate = self.exchange_service.get_rate()
        self.currency_card.set_value(f"{rate.rate:.4f}")
        self.currency_card.set_updated(f"Oppdatert: {rate.timestamp:%H:%M}")

        prices = self.price_service.get_all_prices()
        if not prices:
            return

        total_prices = [
            self.tariff_service.calculate_total_price(price)
            for price in prices
        ]

        items = self.analysis_service.create_timeline(total_prices)
        self.timeline.set_items(items)
