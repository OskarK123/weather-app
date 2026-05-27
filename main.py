from services.openwather_api import get_weather
import time
from services.excel_files import save_to_excel

while True:
    weather = get_weather()
    save_to_excel([weather])
    print("Udało się pobrać dane")
    time.sleep(10)


