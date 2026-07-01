from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:

    # Colors
    background: str = "#F5F6F8"
    surface: str = "#FFFFFF"

    primary: str = "#1976D2"

    text: str = "#202020"
    secondary_text: str = "#707070"

    border: str = "#D8D8D8"

    success: str = "#43A047"
    warning: str = "#FB8C00"
    danger: str = "#E53935"

    # Radius

    radius: int = 12

    # Spacing

    margin: int = 20

    spacing: int = 16