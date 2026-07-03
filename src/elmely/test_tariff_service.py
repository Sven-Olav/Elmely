from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.services.tariff_service import TariffService


def main():

    tariff = TariffService()

    print()
    print("=" * 60)
    print("TARIFF SERVICE TEST")
    print("=" * 60)

    print()

    print(f"Provider........... {tariff.provider_name()}")
    print(f"Price area......... {tariff.price_area()}")

    print()

    print(f"MVA................ {tariff.vat_rate() * 100:.0f} %")
    print(f"Spot markup........ {tariff.spot_markup():.4f} DKK/kWh")

    print()

    print(
        f"Supplier........... "
        f"{tariff.supplier_subscription():.2f} DKK/month"
    )

    print(
        f"Energinet.......... "
        f"{tariff.energinet_subscription():.2f} DKK/month"
    )


if __name__ == "__main__":
    main()