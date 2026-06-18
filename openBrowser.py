from playwright.sync_api import sync_playwright
import config
def openBrowser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            channel="chrome"
        )
        page = browser.new_page()

        page.goto(config.URL)
        page.wait_for_timeout(4000)