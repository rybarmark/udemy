from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "PRG"

def check_destination_code(order):
    if sheet_data[order]["code"] == "":
        for row in sheet_data:
            row["code"] = flight_search.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

order = 0
for destination in sheet_data:
    check_destination_code(order)
    order += 1
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["code"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["price"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only CZK{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
