import os
from dotenv import load_dotenv
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

# --- ADD THESE TWO LINES ---
# This will find and load the variables from your .env file
load_dotenv()
SBR_WEBDRIVER = os.getenv('SBR_WEBDRIVER')
# --- END OF ADDED LINES ---

def scrape_website(website_url):
    """
    Connects to Bright Data's Browser API, navigates to a URL,
    solves CAPTCHAs, and returns the page's HTML source.
    """
    print('Connecting to Scraping Browser...')
    
    # --- CHANGE THIS LINE ---
    # Instead of hardcoding the URL, we now use the variable loaded from the .env file
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    # --- END OF CHANGE ---
    
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print(f'Connected! Navigating to {website_url}...')
        driver.get(website_url)
        
        # This is the official CAPTCHA handling code from Bright Data
        print('Navigated! Waiting captcha to detect and solve...')
        result = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10 * 1000},
        })
        status = result['value']['status']
        print(f'Captcha status: {status}')
        
        print('Scraping page content...')
        html_content = driver.page_source
        
        # Return the content to be used by main.py
        return html_content

# --- All your helper functions remain below this ---

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]









