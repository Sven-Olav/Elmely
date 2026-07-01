import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.ui.widgets.info_card import InfoCard


def main():

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Elmely UI Playground")
    window.resize(600, 400)

    layout = QVBoxLayout(window)

    layout.addWidget(
        InfoCard(
            "Spotpris",
            "0.82 DKK",
            "inkl. moms"
        )
    )

    layout.addWidget(
        InfoCard(
            "Temperatur",
            "18°C",
            "Bornholm"
        )
    )

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()