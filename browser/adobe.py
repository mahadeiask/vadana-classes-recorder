from playwright.sync_api import TimeoutError


def open_adobe(recording_page):
    print("🌐 Waiting for Adobe page...")

    recording_page.wait_for_load_state("domcontentloaded")

    # کمی صبر برای نمایش دیالوگ
    recording_page.wait_for_timeout(3000)

    # فشردن Enter
    recording_page.keyboard.press("Enter")

    print("⌨️ Enter pressed")

    return recording_page
def wait_for_player(adobe_page):
    print("⏳ Waiting for player...")

    try:
        adobe_page.wait_for_selector(
            "#play-recording-shim-button",
            timeout=30000
        )

        print("✅ Player loaded")

    except TimeoutError:
        print("🔄 Timeout, refreshing page...")

        adobe_page.reload()

        adobe_page.wait_for_selector(
            "#play-recording-shim-button",
            timeout=30000
        )

        print("✅ Player loaded after refresh")

def play_recording(adobe_page):
    adobe_page.locator(
        "#play-recording-shim-button"
    ).click()

    print("▶ Recording started")