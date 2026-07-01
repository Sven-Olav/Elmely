from PySide6.QtWidgets import QListWidget


class Navigation(QListWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)

        self.addItem("🏠  Oversikt")
        self.addItem("⚡  Priser")
        self.addItem("🌤  Vær")
        self.addItem("📈  Analyse")
        self.addItem("📅  Historikk")
        self.addItem("📄  Eksport")
        self.addItem("⚙  Innstillinger")

        self.setCurrentRow(0)