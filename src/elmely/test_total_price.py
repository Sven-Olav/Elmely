from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.services.electricity_price_service import ElectricityPriceService
from elmely.services.tariff_service import TariffService


def main():

    price_service = ElectricityPriceService()

    tariff_service = TariffService()

    current_price = price_service.get_current_price()

    if current_price is None:

        print("Fant ingen gjeldende strømpris.")

        return

    total = tariff_service.calculate_total_price(
        current_price
    )

    print()

    print("=" * 60)
    print("TOTAL PRICE TEST")
    print("=" * 60)

    print()

    print(
        f"Time............... "
        f"{total.timestamp:%Y-%m-%d %H:%M}"
    )

    print()

    print(
        f"Spot............... "
        f"{total.spot:.3f} DKK"
    )

    print(
        f"Spot markup........ "
        f"{total.spot_markup:.3f} DKK"
    )

    print(
        f"Network charge..... "
        f"{total.network_charge:.3f} DKK"
    )

    print(
        f"Electricity tax.... "
        f"{total.electricity_tax:.3f} DKK"
    )

    print(
        f"VAT................ "
        f"{total.vat:.3f} DKK"
    )

    print("-" * 60)

    print(
        f"TOTAL.............. "
        f"{total.total:.3f} DKK"
    )


if __name__ == "__main__":
    main()