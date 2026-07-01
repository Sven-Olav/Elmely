from elmely.ui.themes.light_theme import Theme


class ThemeManager:

    _theme = Theme()

    @classmethod
    def current(cls):

        return cls._theme