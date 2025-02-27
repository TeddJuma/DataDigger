# Data Digger
A versatile Python-based web scraper designed to extract various types of data from web pages.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This web scraper is built using Python with the `requests` and `BeautifulSoup` libraries. It provides methods to extract titles, text, images, links, and tables from web pages. For dynamic content, it utilizes Selenium.

## Features
- **Title Extraction**: Extracts the title of a webpage.
- **Text Extraction**: Extracts text from specific HTML elements using CSS selectors.
- **Image Extraction**: Extracts image sources from a webpage.
- **Link Extraction**: Extracts URLs from links on a webpage.
- **Table Extraction**: Extracts data from tables.
- **Dynamic Content Handling**: Uses Selenium to handle web pages with dynamic content.

## Requirements
- Python 3.8+
- `requests`
- `beautifulsoup4`
- `selenium` (for dynamic content)

## Installation
1. Clone the repository:
``` bash
git clone https://github.com/TeddJuma/DataDigger
```
2. Install required libraries:
``` bash
pip install requests beautifulsoup4 selenium
```
3. Download the Selenium WebDriver (e.g., ChromeDriver) and ensure it's in your system's PATH.

## Usage
1. Import the `WebScraper` class in your Python script.
2. Create an instance of `WebScraper` with the target URL.
3. Use methods like `extract_title()`, `extract_text()`, etc., to extract desired data.

## Examples
``` python
from web_scraper import WebScraper

url = "http://example.com"
scraper = WebScraper(url)

html = scraper.fetch_page()
soup = scraper.parse_html(html)

title = scraper.extract_title(soup)
print(f"Title: {title}")

text = scraper.extract_text(soup, "div > p")
print(f"Text: {text}")
```

## Troubleshooting
- **Connection Errors**: Check your internet connection and ensure the target URL is correct.
- **Blocked by Website**: Implement techniques like rotating user agents or using proxies.

## Contributing
Contributions are welcome! Please submit pull requests with detailed explanations of changes.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
