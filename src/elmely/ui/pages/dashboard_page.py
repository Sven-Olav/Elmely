from PySide6.QtWidgets import QWidget, QGridLayout

from elmely.ui.widgets.info_card import InfoCard


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        layout.setSpacing(20)

        layout.addWidget(
            InfoCard(
                "Spotpris",
                "--,-- DKK",
                "inkl. moms",
            ),
            0,
            0,
        )

        layout.addWidget(
            InfoCard(
                "Totalpris",
                "--,-- DKK",
                "inkl. afgifter",
            ),
            0,
            1,
        )

        layout.addWidget(
            InfoCard(
                "Valutakurs",
                "--,--",
                "DKK → NOK",
            ),
            1,
            0,
        )

        layout.addWidget(
            InfoCard(
                "Vær",
                "-- °C",
                "Bornholm",
            ),
            1,
            1,
        )