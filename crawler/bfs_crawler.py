import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import re
import time
import json


class BFSCrawler: #we define a class called bfs crawler
    def __init__(self, seed_url, max_depth=1, delay=0):
        self.seed_url = seed_url
        self.max_depth = max_depth
        self.delay = delay

        self.visited = set() #visited array for the bfs operation
        self.queue = deque()  #queue for the dsa operation
        self.documents = []   #documents to store all the crawled documents.

    def fetch_page(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
            return None

    def parse_html(self, html):
        return BeautifulSoup(html, "html.parser")

    def extract_text(self, soup):
        paragraphs = soup.find_all("p")
        text_content = []

        for p in paragraphs:
            text = p.get_text().strip()
            if len(text) > 50:  # avoid tiny junk paragraphs
                text = re.sub(r"\[\d+\]", "", text)  # remove citations
                text_content.append(text)

        return "\n".join(text_content)

    def is_valid_link(self, url):
        """
        Filter only DSA-related links.
        Modify keywords as needed.
        """
        keywords = [
            "data", "algorithm", "tree", "graph",
            "stack", "queue", "search", "sort",
            "dynamic", "recursion"
        ]

        url_lower = url.lower()
        blacklist = ["tag", "category", "about", "write", "jobs", "login"]

        if any(word in url_lower for word in blacklist):
            return False

        if any(keyword in url_lower for keyword in keywords):
            return True

        return False

    def extract_links(self, soup, base_url):
        links = []

        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            full_url = urljoin(base_url, href)

            # Normalize URL (remove fragments)
            parsed = urlparse(full_url)
            clean_url = parsed.scheme + "://" + parsed.netloc + parsed.path

            if self.is_valid_link(clean_url):
                links.append(clean_url)

        return links[:10]

    def crawl(self):
        self.queue.append((self.seed_url, 0))
        self.visited.add(self.seed_url)

        while self.queue:
            current_url, depth = self.queue.popleft()

            if depth > self.max_depth:
                continue

            print(f"Crawling: {current_url} | Depth: {depth}")

            html = self.fetch_page(current_url)
            if not html:
                continue

            soup = self.parse_html(html)

            title = soup.title.string.strip() if soup.title else "No Title"
            content = self.extract_text(soup)

            self.documents.append({
                "url": current_url,
                "title": title,
                "content": content
            })

            links = self.extract_links(soup, current_url)

            for link in links:
                if link not in self.visited:
                    self.visited.add(link)
                    self.queue.append((link, depth + 1))

            time.sleep(self.delay)  # politeness delay

        return self.documents


if __name__ == "__main__":
    seed = "https://www.geeksforgeeks.org/dsa/deque-set-1-introduction-applications/"
    crawler = BFSCrawler(seed_url=seed, max_depth=2)
    docs = crawler.crawl()

    print(f"\nTotal documents collected: {len(docs)}")
    with open('data/crawled_documents.json', 'w', encoding='utf-8') as f:
        json.dump(docs, f, indent=2)