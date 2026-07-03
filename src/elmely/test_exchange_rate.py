from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.services.exchange_rate_service import ExchangeRateService


def main():

    service = ExchangeRateService()

    #
    # Første kall (API)
    #

    rate = service.get_rate()

    print()

    print("=" * 60)
    print("EXCHANGE RATE TEST")
    print("=" * 60)

    print()

    print(
        f"From............... "
        f"{rate.from_currency}"
    )

    print(
        f"To................. "
        f"{rate.to_currency}"
    )

    print()

    print(
        f"Rate............... "
        f"{rate.rate:.4f}"
    )

    print()

    print(
        f"Timestamp.......... "
        f"{rate.timestamp:%Y-%m-%d %H:%M:%S}"
    )

    #
    # Andre kall (cache)
    #

    print()

    print("Testing cache...")

    cached = service.get_rate()

    print(
        f"Cached rate........ "
        f"{cached.rate:.4f}"
    )


if __name__ == "__main__":
    main()