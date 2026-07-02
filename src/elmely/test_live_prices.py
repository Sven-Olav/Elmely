from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.services.electricity_price_service import (
    ElectricityPriceService,
)


def print_prices(title, prices):

    print()
    print("=" * 60)
    print(title)
    print("=" * 60)

    print(f"Antall priser: {len(prices)}")

    if prices:

        print(f"Første: {prices[0].start}")
        print(f"Siste : {prices[-1].start}")

    print()

    for price in prices:

        print(
            f"{price.start:%Y-%m-%d %H:%M}"
            f"  {price.spot_price_dkk:.3f} DKK/kWh"
        )


def main():

    service = ElectricityPriceService()

    all_prices = service.get_all_prices()
    today_prices = service.get_today_prices()
    tomorrow_prices = service.get_tomorrow_prices()

    print_prices("ALLE PRISER", all_prices)
    print_prices("DAGENS PRISER", today_prices)
    print_prices("MORGENDAGENS PRISER", tomorrow_prices)


if __name__ == "__main__":
    main()