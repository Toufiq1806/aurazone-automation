from playwright.sync_api import sync_playwright

BASE_URL = "https://test.aurazone.shop/"

def test_homepage_loads_with_title():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        page.goto(BASE_URL)

        assert page.title() == "Aurazone - Premium Footwear"

        browser.close()