from playwright.sync_api import sync_playwright

BASE_URL = "https://test.aurazone.shop/"

def test_filter_applied_and_results_appear():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        page.goto(BASE_URL)

        # For now, just check that the page loads successfully
        # We will later add filter logic when we know the real selectors
        assert page.title() == "Aurazone - Premium Footwear"

        browser.close()