from playwright.sync_api import sync_playwright

BASE_URL = "https://test.aurazone.shop/"

def test_container_visible():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        page.goto(BASE_URL)

      
        grid = page.locator("css=div.grid")
        grid.wait_for(state="visible", timeout=5000)

       
        assert grid.is_visible()

        browser.close()