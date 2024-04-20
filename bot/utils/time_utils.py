import time
from datetime import datetime
from random import randint


class TimeUtils:

    @staticmethod
    def sleep_between_1_and_2_seconds():
        time.sleep(1 + randint(1, 1000) / 1000)  # randomize sleeps between actions to simulate human behavior

    @staticmethod
    def sleep_minutes(minutes: int):
        time.sleep(60 * minutes)

    @staticmethod
    def get_current_datetime_string():
        dt_string = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        print("\nCurrent datetime: ", dt_string)
        return dt_string
