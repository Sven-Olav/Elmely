from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class InfoCard(QFrame):

    def __init__(self, title: str, value: str, subtitle: str = ""):
        super().__init__()

        self.setObjectName("InfoCard")

        self.setMinimumSize(260, 180)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(6)

        #
        # Tittel
        #

        self.title_label = QLabel(title)

        title_font = QFont("Segoe UI", 10)
        title_font.setBold(True)

        self.title_label.setFont(title_font)

        #
        # Stor verdi
        #

        self.value_label = QLabel(value)

        value_font = QFont("Segoe UI", 22)
        value_font.setBold(True)

        self.value_label.setFont(value_font)


        #
        # Undertittel
        #

        self.subtitle_label = QLabel(subtitle)

        subtitle_font = QFont("Segoe UI", 9)

        self.subtitle_label.setFont(subtitle_font)

        #
        # Oppdatert
        #

        self.updated_label = QLabel("Oppdatert: --")

        updated_font = QFont("Segoe UI", 8)

        self.updated_label.setFont(updated_font)

        #
        # Layout
        #

        layout.addWidget(self.title_label)

        layout.addStretch()

        layout.addWidget(self.value_label)

        layout.addWidget(self.subtitle_label)

        layout.addStretch()

        layout.addWidget(
            self.updated_label,
            alignment=Qt.AlignmentFlag.AlignRight
        )
    def set_value(self, value: str):

        self.value_label.setText(value)

    def set_subtitle(self, subtitle: str):

        self.subtitle_label.setText(subtitle)

    def set_updated(self, updated: str):

        self.updated_label.setText(updated)