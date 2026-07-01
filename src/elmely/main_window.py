from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QMainWindow,
    QWidget,
    QStatusBar,
)

from elmely import APP_NAME, VERSION
from elmely.ui.navigation import Navigation


class MainWindow(QMainWindow):

    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 900

    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"{APP_NAME} {VERSION}")
        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        self._create_ui()

        self.statusBar().showMessage("Ready")

    def _create_ui(self):

        root = QWidget()

        layout = QHBoxLayout(root)

        self.navigation = Navigation()

        self.content = QLabel("Velkommen til Elmely Energy Monitor")
        self.content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.navigation)
        layout.addWidget(self.content, 1)

        self.setCentralWidget(root)

        self.setStatusBar(QStatusBar())