# sync (not async) - po kolei, jeden proces blokuje następny; async - jednocześnie, jeden proces nie blokuje następnego
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # start browser
    browser = p.chromium.launch(headless=False)
    # open new page
    page = browser.new_page()
    # got to page
    page.goto("http://onet.pl")
    # get page title
    page_title = page.title()
    # display page title in console
    print(f"Tytul strony to {page_title}.")

    assert "Onet – Jesteś na bieżąco" in page_title

    # close browser, kill all processes
    browser.close()