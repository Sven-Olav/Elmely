from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from elmely.services.nordpool_service import NordPoolService


service = NordPoolService()

prices = service.get_today_prices()

for price in prices:

    print(price)