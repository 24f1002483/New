from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath('index.html')

        # Go to the local HTML file
        page.goto(f'file://{file_path}')

        # Make a few moves to get a winning state
        page.click('[data-cell-index="0"]')  # X
        page.click('[data-cell-index="3"]')  # O
        page.click('[data-cell-index="1"]')  # X
        page.click('[data-cell-index="4"]')  # O
        page.click('[data-cell-index="2"]')  # X wins

        # Take a screenshot
        page.screenshot(path="jules-scratch/verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run()