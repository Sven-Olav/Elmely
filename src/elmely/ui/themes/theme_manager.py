from pathlib import Path

from elmely.ui.themes.light_theme import Theme


class ThemeManager:

    _theme = Theme()

    @classmethod
    def current(cls):
        return cls._theme

    @classmethod
    def load_stylesheet(cls) -> str:

        stylesheet = (
            Path(__file__).parent / "light.qss"
        )

        return stylesheet.read_text(encoding="utf-8")