from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.services.analysis_service import AnalysisService
from elmely.services.electricity_price_service import ElectricityPriceService
from elmely.services.tariff_service import TariffService


def main():

    print()
    print("=" * 60)
    print("PRICE ANALYSIS TEST")
    print("=" * 60)
    print()

    #
    # Hent strømpriser
    #

    price_service = ElectricityPriceService()

    prices = price_service.get_today_prices()

    if not prices:
        print("Fant ingen priser.")
        return

    #
    # Beregn totalpriser
    #

    tariff = TariffService()

    total_prices = [
        tariff.calculate_total_price(price)
        for price in prices
    ]

    #
    # Analyse
    #

    analysis = AnalysisService()

    for hours in [1, 2, 3, 5]:

        period = analysis.find_cheapest_period(
            total_prices,
            hours,
        )

        print(f"{hours} time(r)")
        print("-" * 30)

        print(
            f"Start........ {period.start:%Y-%m-%d %H:%M}"
        )

        print(
            f"Slutt........ {period.end:%Y-%m-%d %H:%M}"
        )

        print(
            f"Gjennomsnitt. {period.average_price:.3f} DKK/kWh"
        )

        print()


if __name__ == "__main__":
    main()