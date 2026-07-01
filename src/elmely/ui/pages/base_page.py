from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class BasePage(QWidget):

    def __init__(self, title: str):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel(title)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Litt større overskrift
        font = label.font()
        font.setPointSize(20)
        font.setBold(True)
        label.setFont(font)

        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()