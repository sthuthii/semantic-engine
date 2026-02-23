import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    """
    Docstring for fetch_url
    
    :param url: Description
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def parse_html(html):
    """
    Docstring for parse_html
    
    :param html: Description
    """
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_title(soup):
    """
    Docstring for extract_title
    
    :param soup: Description
    """
    title = soup.title.string.strip()
    if soup.title:
        return title
    return "No title found."

def extract_paragraphs(soup):
    """
    Docstring for extract_paragraphs
    
    :param soup: Description
    """
    paragraphs = soup.find_all('p')
    
    text_content = []
    for p in paragraphs:
        text = p.get_text().strip()
        if text:
            text_content.append(text)

    return '\n'.join(text_content)

def scrape_page(url):
    """
    Docstring for scrape_page
    
    :param url: Description
    """
    html = fetch_url(url)
    parse = parse_html(html)

    title = extract_title(parse)
    content = extract_paragraphs(parse)

    return {
        'title' : title,
        'content': content
    }

if __name__ == "__main__":
    url = "https://www.geeksforgeeks.org/dsa/introduction-to-binary-tree/"
    result = scrape_page(url)

    print(f"The title of the page is: {result['title']}")
    print(f"The content of the page is: {result['content'][:1000]}...")