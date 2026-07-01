from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QGridLayout

from elmely.ui.widgets.info_card import InfoCard


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setHorizontalSpacing(25)
        layout.setVerticalSpacing(25)

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