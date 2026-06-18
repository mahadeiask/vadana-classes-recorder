def open_my_courses(page):
    page.locator("text=درس‌های من").click()
    page.wait_for_timeout(3000)


def get_courses(page):
    course_links = page.locator(
        "table.generalbox tbody tr td.c1 a"
    )

    count = course_links.count()

    print(f"Found {count} courses")

    courses = []

    for i in range(count):
        link = course_links.nth(i)

        courses.append({
            "title": link.inner_text(),
            "url": link.get_attribute("href")
        })

    return courses