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

        page = context.new_page()

        login(page)

        open_my_courses(page)

        courses = get_courses(page)

        for course in courses:
            print(f"\n📘 {course['title']}")

            recordings = open_recordings(
                page,
                course["url"]
            )

            print(f"🎬 {len(recordings)} recordings found")

        input("\nPress Enter to exit...")

        context.close()


if __name__ == "__main__":
    main()