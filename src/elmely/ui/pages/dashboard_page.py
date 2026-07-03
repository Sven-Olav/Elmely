from datetime import datetime

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QGridLayout, QWidget

from elmely.services.electricity_price_service import ElectricityPriceService
from elmely.ui.widgets.info_card import InfoCard


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        #
        # Service
        #

        self.service = ElectricityPriceService()

        #
        # Layout
        #

        layout = QGridLayout(self)

        layout.setContentsMargins(30, 30, 30, 30)
        layout.setHorizontalSpacing(25)
        layout.setVerticalSpacing(25)

        #
        # Spotpris
        #

        self.spot_card = InfoCard(
            "Spotpris",
            "--,-- DKK",
            "inkl. moms",
        )

        layout.addWidget(self.spot_card, 0, 0)

        #
        # Totalpris
        #

        self.total_card = InfoCard(
            "Totalpris",
            "--,-- DKK",
            "inkl. afgifter",
        )

        layout.addWidget(self.total_card, 0, 1)

        #
        # Valutakurs
        #

        self.currency_card = InfoCard(
            "Valutakurs",
            "--,--",
            "DKK → NOK",
        )

        layout.addWidget(self.currency_card, 1, 0)

        #
        # Vær
        #

        self.weather_card = InfoCard(
            "Vær",
            "-- °C",
            "Bornholm",
        )

        layout.addWidget(self.weather_card, 1, 1)

        #
        # Første oppdatering
        #

        self.update_dashboard()

        #
        # Automatisk oppdatering hvert 5. minutt
        #

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.update_dashboard)

        self.timer.start(5 * 60 * 1000)

    def update_dashboard(self):

        #
        # Hent nye priser
        #

        self.service.refresh()

        current_price = self.service.get_current_price()

        if current_price:

            self.spot_card.set_value(
                f"{current_price.spot_price_dkk:.3f} DKK"
            )

        self.spot_card.set_updated(
            f"Oppdatert: {datetime.now():%H:%M}"
        )