from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class PlaceholderPage(QWidget):

    def __init__(self, title: str):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel(title)

        font = QFont()
        font.setPointSize(22)
        font.setBold(True)

        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()