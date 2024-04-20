from playwright.sync_api import Playwright

from bot.target_page import open_page_and_check_if_termins_are_available
from bot.utils.speech_utils import SpeechUtils
from bot.utils.time_utils import TimeUtils


def test_catch_termin(playwright: Playwright):
    try:
        termins_are_available: bool = open_page_and_check_if_termins_are_available(playwright)
        if termins_are_available:
            SpeechUtils.say("What a luck! There are termins! Get up, you lazy bastard!")
            print("There are termins!!!")
            TimeUtils.sleep_minutes(20)  # do not close browser window, to be able to book a termin manually
        else:
            # SpeechUtils.say("No termins. What do you expect?")  # uncomment only for the sound test
            pass
    except Exception as e:
        SpeechUtils.say("Your script is broken! Get up and write some stable code!")
        print(f"Exception: {e}")
