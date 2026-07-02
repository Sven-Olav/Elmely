from datetime import datetime

from PySide6.QtWidgets import QGridLayout, QWidget

from elmely.services.electricity_price_service import ElectricityPriceService
from elmely.ui.widgets.info_card import InfoCard


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

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

        layout.addWidget(
            InfoCard(
                "Totalpris",
                "--,-- DKK",
                "inkl. afgifter",
            ),
            0,
            1,
        )

        #
        # Valutakurs
        #

        layout.addWidget(
            InfoCard(
                "Valutakurs",
                "--,--",
                "DKK → NOK",
            ),
            1,
            0,
        )

        #
        # Vær
        #

        layout.addWidget(
            InfoCard(
                "Vær",
                "-- °C",
                "Bornholm",
            ),
            1,
            1,
        )

        #
        # Live strømpris
        #

        service = ElectricityPriceService()

        prices = service.get_today_prices()

        now = datetime.now()

        current_price = None

        for price in prices:

            if price.start <= now < price.end:

                current_price = price
                break

        if current_price:

            self.spot_card.set_value(
                f"{current_price.spot_price_dkk:.3f} DKK"
            )

            self.spot_card.set_updated(
                f"Live {now:%H:%M}"
            )

        elif prices:

            #
            # Fallback dersom vi er utenfor intervallet
            #

            self.spot_card.set_value(
                f"{prices[0].spot_price_dkk:.3f} DKK"
            )

            self.spot_card.set_updated("Live")