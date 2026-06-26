import traceback
from playwright.sync_api import TimeoutError
import pyautogui
import time
from recorder.obs import (
    start_recording,
    )
from config import END_KEYWORDS


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

    adobe_page.wait_for_timeout(30000)
    
    adobe_page.keyboard.press("Tab")

    adobe_page.wait_for_timeout(500)

    adobe_page.keyboard.press("Enter")

    print("▶ Recording started")


import traceback

import traceback

def get_last_chat_message(adobe_page):
    try:
        # صبر کن iframe لود شود
        adobe_page.wait_for_selector("#html-meeting-frame", timeout=10000)

        # وارد iframe شو
        frame = adobe_page.frame_locator("#html-meeting-frame")

        # پیام‌ها
        messages = frame.locator("#chatIndividualMessage")

        # اگر هنوز پیامی نیست
        if messages.count() == 0:
            return None

        # آخرین پیام
        last = messages.last

        sender = last.locator("#chatMessageSender").text_content()
        text = last.locator("#chatIndividualMessageContent").text_content()

        sender = sender.strip() if sender else ""
        text = text.strip() if text else ""

        return {
            "sender": sender,
            "text": text
        }

    except Exception as e:
        print(f"ERROR: {type(e).__name__}")
        print(e)
        traceback.print_exc()
        return None
def should_stop_recording(message):
    if message is None:
        return False

    text = message["text"]

    for keyword in END_KEYWORDS:
        if keyword in text:
            return True

    return False