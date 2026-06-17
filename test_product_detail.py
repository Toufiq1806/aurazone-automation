from playwright.sync_api import sync_playwright

BASE_URL = "https://test.aurazone.shop/"

def test_product_detail_page_opens_after_click():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        page.goto(BASE_URL)

        
        first_product_title = page.locator("css=h3[title]").first
        first_product_title.click()
        page.wait_for_load_state("networkidle")

       
        title = page.title()
        assert title is not None and len(title) > 0

        browser.close()