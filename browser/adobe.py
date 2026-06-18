from playwright.sync_api import TimeoutError


def open_in_browser(recording_page):
    print("🌐 Waiting for Adobe page...")

    recording_page.wait_for_load_state("domcontentloaded")

    # بستن پنجرهٔ باز کردن برنامه
    try:
        cancel_button = recording_page.locator(
            'button:has-text("Cancel")'
        )

        cancel_button.wait_for(timeout=5000)

        cancel_button.click()

        print("❌ Open app popup closed")

    except TimeoutError:
        print("ℹ️ No popup found")

    # کلیک روی Open in browser
    open_button = recording_page.locator(
        'a:has-text("Open in browser")'
    )

    open_button.wait_for(timeout=10000)

    with recording_page.expect_popup() as popup_info:
        open_button.click()

    adobe_page = popup_info.value

    adobe_page.wait_for_load_state()

    print("✅ Adobe opened in browser")

    return adobe_page


def wait_for_player(adobe_page):
    print("⏳ Waiting for player...")

    try:
        adobe_page.wait_for_selector(
            "#play-recording-shim-button",
            timeout=30000
        )

        return True

    except TimeoutError:
        print("🔄 Refreshing page...")

        adobe_page.reload()

        adobe_page.wait_for_selector(
            "#play-recording-shim-button",
            timeout=30000
        )

        return True
    
def play_recording(adobe_page):
    play_button = adobe_page.locator(
        "#play-recording-shim-button"
    )

    play_button.click()

    print("▶ Recording started")

