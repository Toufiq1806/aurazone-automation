# AuraZone QA Automation (Playwright + Python)

Basic automation tests for **https://test.aurazone.shop/** using **Playwright** and **pytest**.

These tests validate core e-commerce flows such as:
- Homepage load and title
- Product listing page
- Filter functionality
- Product detail page
- Cart interaction (basic)

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A modern browser 

## Project Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Toufiq1806/aurazone-automation.git
   cd aurazone-automation
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```bash
   playwright install
   ```

### Run a specific test

```bash
pytest test_homepage.py -v
```

```bash
pytest test_product_listing.py -v
```

```bash
pytest test_filter.py -v
```

```bash
pytest test_product_detail.py -v
```

```bash
pytest test_cart.py -v
```

## Project Structure

```text
aurazone-automation/

    test_homepage.py        # Test: homepage loads with correct title
    test_product_listing.py # Test: product listing grid exists
    test_filter.py          # Test: page loads (basic filter test)
    test_product_detail.py  # Test: product detail page opens after click
    test_cart.py            # Test: basic product click flow
    requirements.txt        # Python dependencies
    README.md               # This readme file
```

## Test Cases

| Test File              | Description                                            |
|------------------------|--------------------------------------------------------|
| `test_homepage.py`     | Verify homepage loads and has correct page title      |
| `test_product_listing.py` | Verify product listing grid exists on the homepage |
| `test_filter.py`       | Basic test: page loads successfully                   |
| `test_product_detail.py` | Click first product and verify detail page opens    |
| `test_cart.py`         | Basic product click flow      |

## Technologies Used

- **Language**: Python  
- **Framework**: Playwright (for browser automation)  
- **Test Runner**: pytest  
- **Target Application**: https://test.aurazone.shop/

Author


Made by Mohamed Toufiq
