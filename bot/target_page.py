from playwright.sync_api import Playwright, Page, Browser, ElementHandle

from bot.utils.screenshots_utils import ScreenshotsUtils
from bot.utils.time_utils import TimeUtils

START_URL: str = "https://tevis.ekom21.de/stdar/select2?md=3"
PATH_TO_SCREENSHOTS: str = "/Users/vmoloko/Desktop/termin-catcher-data"


def open_page_and_check_if_termins_are_available(playwright: Playwright) -> bool:
    browser: Browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    page: Page = browser.new_page()
    page.goto(START_URL)
    TimeUtils.sleep_between_1_and_2_seconds()
    page.get_by_text("Ablehnen").click()
    TimeUtils.sleep_between_1_and_2_seconds()
    page.get_by_text("Erteilung/Ersatz/Umtausch").click()
    TimeUtils.sleep_between_1_and_2_seconds()
    page.locator(
        "//button[@aria-label='Erhöhen der Anzahl des Anliegens Antrag Umschreibung einer ausländischen Fahrerlaubnis']").click()
    TimeUtils.sleep_between_1_and_2_seconds()
    page.locator("//input[@aria-label='Weiter']").click()
    TimeUtils.sleep_between_1_and_2_seconds()
    page.get_by_title("OK").click()
    TimeUtils.sleep_between_1_and_2_seconds()
    page.locator("//input[@aria-label='Bürger- und Ordnungsamt (Luisencenter) auswählen']").click()
    TimeUtils.sleep_between_1_and_2_seconds()
    ScreenshotsUtils.make_screenshot(
        page,
        f"{PATH_TO_SCREENSHOTS}/{TimeUtils.get_current_datetime_string()}.png"
    )
    no_termins_element: ElementHandle = page.query_selector("text='Kein freier Termin verfügbar'")
    return no_termins_element is None
