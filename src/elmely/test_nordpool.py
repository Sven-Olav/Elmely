from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.services.electricity_price_service import NordPoolService


service = NordPoolService()

prices = service.get_today_prices()

for price in prices:
    print(
        f"{price.start:%H:%M} - "
        f"{price.end:%H:%M} : "
        f"{price.spot_price_dkk:.2f} DKK/kWh"
    )