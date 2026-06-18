from config import URL, USERNAME, PASSWORD

def login(page):
    page.goto(URL)
    page.wait_for_timeout(3000)

    username = page.locator('input[name="username"]')
    password = page.locator('input[name="password"]')

    if username.count() > 0 and password.count() > 0:
        username.fill(USERNAME)
        password.fill(PASSWORD)

        page.click('button[type="button"], input[type="loginBtn"]')

        page.wait_for_timeout(5000)

    print("✅ Login completed")
