from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QMainWindow,
    QStatusBar,
    QWidget,
)

from elmely import APP_NAME, VERSION
from elmely.ui.navigation import Navigation
from elmely.ui.themes.theme_manager import ThemeManager
from elmely.ui.widgets.info_card import InfoCard
from elmely.ui.pages.dashboard_page import DashboardPage

class MainWindow(QMainWindow):

    WINDOW_WIDTH = 1900
    WINDOW_HEIGHT = 780

    def __init__(self):
        super().__init__()

        self.theme = ThemeManager.current()

        self.setWindowTitle(f"{APP_NAME} {VERSION}")
        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        self._create_ui()
        self._create_statusbar()

    def _create_ui(self):

        root = QWidget()

        layout = QHBoxLayout(root)

        layout.setContentsMargins(
            self.theme.margin,
            self.theme.margin,
            self.theme.margin,
            self.theme.margin,
        )

        layout.setSpacing(self.theme.spacing)

        # Venstremeny
        self.navigation = Navigation()
        layout.addWidget(self.navigation)

        # Høyre innhold
        layout.addWidget(DashboardPage(), 1)

        self.setCentralWidget(root)

    def _create_statusbar(self):

        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)