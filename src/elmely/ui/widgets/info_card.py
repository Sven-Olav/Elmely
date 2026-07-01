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

        self.setMinimumWidth(260)
        self.setMinimumHeight(160)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(8)

        # ---------- Title ----------

        title_label = QLabel(title)

        title_font = QFont()
        title_font.setPointSize(10)
        title_font.setBold(True)

        title_label.setFont(title_font)

        # ---------- Value ----------

        value_label = QLabel(value)

        value_font = QFont()
        value_font.setPointSize(24)
        value_font.setBold(True)

        value_label.setFont(value_font)

        value_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # ---------- Subtitle ----------

        subtitle_label = QLabel(subtitle)

        subtitle_font = QFont()
        subtitle_font.setPointSize(9)

        subtitle_label.setFont(subtitle_font)

        layout.addWidget(title_label)

        layout.addStretch()

        layout.addWidget(value_label)

        layout.addWidget(subtitle_label)

        