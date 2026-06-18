# from playwright.sync_api import sync_playwright

# URL = "https://vadana21.ec.iau.ir/p/4042/my/courses.php"

# USERNAME = "403553065"
# PASSWORD = "403553065"


# def open_recordings(page, course_url):
#     page.goto(course_url)
#     page.wait_for_timeout(4000)

#     print(f"\n📘 Opening course: {course_url}")

#     entry_link = page.locator('a:has-text("مشاهده برنامه کلاسی و آرشیو جلسات")')

#     if entry_link.count() == 0:
#         print("❌ Entry link not found")
#         return None

#     with page.expect_popup() as popup_info:
#         entry_link.first.click()

#     page2 = popup_info.value
#     page2.wait_for_load_state()

#     print("✅ Opened class info page")

#     # رفتن به آرشیو جلسات
#     page2.locator('a:has-text("آرشیو جلسات")').click()
#     page2.wait_for_timeout(3000)

#     rows = page2.locator("table.generaltable tbody tr")

#     count = rows.count()
#     print(f"🎬 Found {count} recordings")

#     recordings = []

#     for i in range(count):
#         row = rows.nth(i)

#         date = row.locator("td.c1").inner_text()
#         duration = row.locator("td.c2").inner_text()
#         link = row.locator("td.c3 a").get_attribute("href")

#         recordings.append({
#             "date": date,
#             "duration": duration,
#             "url": link
#         })

#         print(f"{i+1}. {date} | {duration}")
#     # بعد از گرفتن recordings
#     open_first_recording(page2, recordings)

#     return recordings

# def open_first_recording(page2, recordings):
#     rows = page2.locator("table.generaltable tbody tr")

#     count = rows.count()

#     if count == 0:
#         print("❌ No recordings to open")
#         return

#     print("▶ Opening first recording...")

#     first_row = rows.nth(0)
#     link = first_row.locator('td.c3 a')

#     url = link.get_attribute("href")

#     print("🎬 Opening:", url)

#     with page2.expect_popup() as popup_info:
#         link.click()

#     recording_page = popup_info.value
#     recording_page.wait_for_load_state()

#     print("✅ Recording opened")
    

#     return recording_page

# def run():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(
#             headless=False,
#             channel="chrome"
#         )

#         page = browser.new_page()

#         page.goto(URL)
#         page.wait_for_timeout(4000)

#         # login
#         username = page.locator('input[name="username"]')
#         password = page.locator('input[name="password"]')

#         if username.count() > 0 and password.count() > 0:
#             username.fill(USERNAME)
#             password.fill(PASSWORD)

#             page.click('button[type="button"], input[type="loginBtn"]')
#             page.wait_for_timeout(6000)

#         # ورود به "درس‌های من"
#         page.locator('text=درس‌های من').click()
#         page.wait_for_timeout(3000)

#         # گرفتن کلاس‌ها
#         course_links = page.locator('table.generaltable tbody tr td.c1 a')

#         count = course_links.count()
#         print(f"Found {count} courses\n")

#         courses = []

#         for i in range(count):
#             link = course_links.nth(i)

#             courses.append({
#                 "title": link.inner_text(),
#                 "url": link.get_attribute("href")
#             })

#         # 🔥 اینجا مرحله مهم اضافه شد
#         for course in courses:
#             print("\n========================")
#             print(course["title"])

#             recordings = open_recordings(page, course["url"])

#             if recordings:
#                 print(f"✔ {len(recordings)} sessions found")

#         input("Press Enter to exit...")
#         browser.close()


# if __name__ == "__main__":
#     run()
