import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.main_window import MainWindow
from elmely.version import APP_NAME, ORGANIZATION, DOMAIN


def main():

    app = QApplication(sys.argv)

    app.setApplicationName(APP_NAME)
    app.setOrganizationName(ORGANIZATION)
    app.setOrganizationDomain(DOMAIN)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()