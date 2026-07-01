from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class InfoCard(QFrame):

    def __init__(self, title: str, value: str, subtitle: str = ""):
        super().__init__()

        self.setMinimumSize(220, 140)
        self.setMaximumHeight(140)

        self.setObjectName("InfoCard")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)

        self.title = QLabel(title)

        self.value = QLabel(value)

        self.subtitle = QLabel(subtitle)

        value_font = self.value.font()
        value_font.setPointSize(20)
        value_font.setBold(True)

        self.value.setFont(value_font)

        self.value.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.value)
        layout.addWidget(self.subtitle)

        self.setStyleSheet("""
        QFrame#InfoCard {

            background: white;

            border: 1px solid #DADADA;

            border-radius: 12px;

        }

        QLabel {

            border: none;

            background: transparent;

        }
        """)