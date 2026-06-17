from playwright.sync_api import sync_playwright

URL = "https://vadana21.ec.iau.ir/p/4042/my/courses.php"

USERNAME = ""
PASSWORD = ""


def run():
    with sync_playwright() as p:

        # 👇 استفاده از Chrome واقعی سیستم
        browser = p.chromium.launch(
            headless=False,
            channel="chrome"
        )

        page = browser.new_page()

        # رفتن به سایت
        page.goto(URL)
        print("Page opened")

        page.wait_for_timeout(3000)

        # بررسی وجود فیلد لاگین
        username_input = page.locator('input[name="username"]')
        password_input = page.locator('input[name="password"]')

        if username_input.count() > 0 and password_input.count() > 0:
            print("Login page detected")

            username_input.fill(USERNAME)
            password_input.fill(PASSWORD)

            page.click('button[type="button"], input[type="loginBtn"]')

            print("Login submitted")

        # صبر برای ورود
        page.wait_for_timeout(5000)

        print("Current URL:", page.url)

        input("Press Enter to close...")
        browser.close()


if __name__ == "__main__":
    run()