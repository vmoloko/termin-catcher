from playwright.sync_api import Page


class ScreenshotsUtils:
    @staticmethod
    def make_screenshot(page: Page, path_and_name: str):
        page.screenshot(path=path_and_name)
