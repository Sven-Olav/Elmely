from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from elmely.models.timeline_marker import TimelineMarker


@dataclass(slots=True)
class TimelineItem:
    """
    Ett element i prisprognosen.
    """

    #
    # Tid
    #

    timestamp: datetime

    #
    # Priser (DKK/kWh)
    #

    total_price: float = 0.0
    spot_price: float = 0.0
    markup: float = 0.0
    network_charge: float = 0.0
    electricity_tax: float = 0.0
    vat: float = 0.0

    #
    # Analyse
    #

    relative_level: int = 1
    marker: TimelineMarker = TimelineMarker.NORMAL

    def tooltip_text(self) -> str:
        """
        Returnerer HTML-formatert tooltip.
        """

        end_hour = (self.timestamp.hour + 1) % 24

        html = f"""
        <b>{self.timestamp:%H}:00–{end_hour:02d}:00</b><br><br>

        <b>Totalpris</b>&nbsp;&nbsp;&nbsp;
        {self.total_price:.2f} DKK/kWh

        <br><br>

        <table cellspacing="1" cellpadding="2">

        <tr>
            <td>Spotpris</td>
            <td align="right">{self.spot_price:.2f}</td>
            <td>&nbsp;DKK</td>
        </tr>

        <tr>
            <td>Påslag</td>
            <td align="right">{self.markup:.2f}</td>
            <td>&nbsp;DKK</td>
        </tr>

        <tr>
            <td>Nettleie</td>
            <td align="right">{self.network_charge:.2f}</td>
            <td>&nbsp;DKK</td>
        </tr>

        <tr>
            <td>Elavgift</td>
            <td align="right">{self.electricity_tax:.2f}</td>
            <td>&nbsp;DKK</td>
        </tr>

        <tr>
            <td>MVA</td>
            <td align="right">{self.vat:.2f}</td>
            <td>&nbsp;DKK</td>
        </tr>

        </table>
        """

        if self.marker == TimelineMarker.CHEAP:

            html += (
                "<br><br>"
                "⭐ Under valgt billiggrense"
            )

        elif self.marker == TimelineMarker.EXPENSIVE:

            html += (
                "<br><br>"
                "❗ Over valgt prisgrense"
            )

        return html