import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.core.logger import log
from elmely.main_window import MainWindow
from elmely.ui.themes.theme_manager import ThemeManager
from elmely.version import (
    APP_NAME,
    DOMAIN,
    ORGANIZATION,
)


def main():

    log.info("Starting Elmely Energy Monitor")

    app = QApplication(sys.argv)

    app.setStyleSheet(
        ThemeManager.load_stylesheet()
    )

    app.setApplicationName(APP_NAME)
    app.setOrganizationName(ORGANIZATION)
    app.setOrganizationDomain(DOMAIN)

    window = MainWindow()

    window.show()

    log.info("Application started")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()