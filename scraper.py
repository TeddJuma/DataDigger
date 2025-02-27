import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        try:
            response = requests.get(self.url)
            return response.text
        except Exception as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def extract_title(self, soup):
        title = soup.find('title')
        if title:
            return title.text
        return None

    def extract_text(self, soup, selector):
        elements = soup.select(selector)
        return [element.text.strip() for element in elements]

    def extract_images(self, soup):
        images = soup.find_all('img')
        return [img.get('src') for img in images]

    def extract_links(self, soup):
        links = soup.find_all('a')
        return [link.get('href') for link in links]

    def extract_tables(self, soup):
        tables = soup.find_all('table')
        data = []
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all(['th', 'td'])
                cols = [col.text.strip() for col in cols]
                data.append(cols)
        return data

    def handle_dynamic_content(self):
        # Use Selenium for dynamic content
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        # Wait for content to load
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
        html = driver.page_source
        driver.quit()
        return html

# Example usage
if __name__ == "__main__":
    url = "http://example.com"
    scraper = WebScraper(url)
    
    # Fetch and parse HTML
    html = scraper.fetch_page()
    if html:
        soup = scraper.parse_html(html)
        
        # Extract title
        title = scraper.extract_title(soup)
        print(f"Title: {title}")
        
        # Extract specific text
        selector = "div > p"
        text = scraper.extract_text(soup, selector)
        print(f"Text: {text}")
        
        # Extract images
        images = scraper.extract_images(soup)
        print(f"Images: {images}")
        
        # Extract links
        links = scraper.extract_links(soup)
        print(f"Links: {links}")
        
        # Extract tables
        tables = scraper.extract_tables(soup)
        print(f"Tables: {tables}")
        
        # Handle dynamic content if needed
        # dynamic_html = scraper.handle_dynamic_content()
        # dynamic_soup = scraper.parse_html(dynamic_html)
        # # Extract data from dynamic content
