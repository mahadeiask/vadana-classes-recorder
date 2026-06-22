from playwright.sync_api import TimeoutError
import pyautogui
import time


def open_adobe(recording_page):
    print("🌐 Waiting for Adobe page...")

    recording_page.wait_for_load_state("domcontentloaded")

    # کمی صبر برای نمایش دیالوگ
    recording_page.wait_for_timeout(3000)


    # فشردن Enter
    time.sleep(5)

    pyautogui.press("enter")
    recording_page.keyboard.press("Enter")
    # recording_page.bring_to_front()
    print("⌨️ Enter pressed")
    return recording_page

def wait_for_player(adobe_page):
    print("⏳ Waiting for player...")

    try:
        adobe_page.wait_for_selector(
            'a[onclick="openMeetingInHtmlClient()"]',
            timeout=20000
        )
        adobe_page.click('a:has-text("Open in browser")')

        print("✅ Player loaded")

    except TimeoutError:
        print("🔄 Timeout, refreshing page...")
        adobe_page.back()

        adobe_page.reload()

        adobe_page.wait_for_selector(
            'a[onclick="openMeetingInHtmlClient()"]',
            timeout=30000
        )
        adobe_page.click('a:has-text("Open in browser")')

        print("✅ Player loaded after refresh")

def play_recording(adobe_page):
    adobe_page.wait_for_load_state("domcontentloaded")

    adobe_page.bring_to_front()

    # یک کلیک روی فضای خالی صفحه برای گرفتن فوکوس
    adobe_page.mouse.click(200, 200)

    adobe_page.wait_for_timeout(1000)

    adobe_page.keyboard.press("Tab")

    adobe_page.wait_for_timeout(500)
    adobe_page.keyboard.press("Tab")

    adobe_page.wait_for_timeout(500)
    adobe_page.keyboard.press("Tab")

    adobe_page.wait_for_timeout(500)
    adobe_page.keyboard.press("Tab")

    adobe_page.wait_for_timeout(500)
    adobe_page.keyboard.press("Tab")

    adobe_page.wait_for_timeout(20000)
    
    adobe_page.keyboard.press("Tab")

    adobe_page.wait_for_timeout(500)

    adobe_page.keyboard.press("Enter")

    print("▶ Recording started")