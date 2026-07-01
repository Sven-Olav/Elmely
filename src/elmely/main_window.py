from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QStatusBar,
    QWidget,
)

from elmely import APP_NAME, VERSION
from elmely.ui.navigation import Navigation
from elmely.ui.pages.dashboard_page import DashboardPage
from elmely.ui.pages.placeholder_page import PlaceholderPage
from elmely.ui.themes.theme_manager import ThemeManager


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

        #
        # Navigation
        #

        self.navigation = Navigation()

        #
        # Pages
        #

        self.pages = QStackedWidget()

        self.pages.addWidget(DashboardPage())
        self.pages.addWidget(PlaceholderPage("⚡ Priser"))
        self.pages.addWidget(PlaceholderPage("🌤 Vær"))
        self.pages.addWidget(PlaceholderPage("📈 Analyse"))
        self.pages.addWidget(PlaceholderPage("📅 Historikk"))
        self.pages.addWidget(PlaceholderPage("📄 Eksport"))
        self.pages.addWidget(PlaceholderPage("⚙ Innstillinger"))

        #
        # Connect signals
        #

        self.navigation.currentRowChanged.connect(
            self.pages.setCurrentIndex
        )

        #
        # Layout
        #

        layout.addWidget(self.navigation)
        layout.addWidget(self.pages, 1)

        self.setCentralWidget(root)

    def _create_statusbar(self):

        status = QStatusBar()
        status.showMessage("Ready")

        self.setStatusBar(status)