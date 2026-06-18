from playwright.sync_api import sync_playwright

from browser.login import login
from browser.courses import open_my_courses, get_courses
from browser.recordings import open_recordings


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False
        )

        context = browser.new_context()

        page = context.new_page()

        login(page)

        open_my_courses(page)

        courses = get_courses(page)
    for course in courses:
        print(f"\n📘 {course['title']}")

        archive_page, recordings = open_recordings(
            page,
            course["url"]
        )

        print(f"🎬 {len(recordings)} recordings found")

    for recording in recordings:
        print(
            f"▶ {recording['date']} | "
            f"{recording['duration']}"
        )

        archive_page.goto(recording["url"])

        archive_page.wait_for_load_state()
        input("\nPress Enter to exit...")

        context.close()
        browser.close()


if __name__ == "__main__":
    main()