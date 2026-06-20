def open_recordings(page, course_url):
    page.goto(course_url)

    page.wait_for_timeout(4000)

    entry_link = page.locator(
        'a:has-text("مشاهده برنامه کلاسی و آرشیو جلسات")'
    )

    if entry_link.count() == 0:
        return None, []

    with page.expect_popup() as popup_info:
        entry_link.first.click()

    page2 = popup_info.value
    page2.wait_for_load_state()

    recordings_tab = page2.locator(
        'a:has-text("آرشیو جلسات")'
    )

    recordings_tab.click()

    page2.wait_for_timeout(3000)

    rows = page2.locator(
        "table.generaltable tbody tr"
    )

    recordings = []

    for i in range(rows.count()):
        row = rows.nth(i)

        recordings.append({
            "date": row.locator("td.c1").inner_text(),
            "duration": row.locator("td.c2").inner_text(),
            "url": row.locator("td.c3 a").get_attribute("href")
        })

    return page2, recordings