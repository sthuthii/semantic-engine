Day 1 — How Search Engines Work
Learn
•	Crawler
A crawler is an automated or program that systematically browses the web pages, in the world wide web. This is what a search engine uses to discover and index web pages, ensuring up to date results.
Initially a crawler starts with seed websites, or known websites, it requests the page content, renders the content, and then scans the page for more URLs. It indexes or stores all the visited web pages in the search engine’s database.
It checks the website’s robots.txt file to check if the website is accessible or not.
Example: web spider bot, bot
•	Indexer
It is a core component that processes, parses and organises data collected by crawlers into a structured, searchable database called an index.
Key functions of an indexer:
Data analysis and parsing: Extracts, filters and analyses text documents where they appear, performs stemming.
Creating the inverted index: It maps the keywords to specific documents where they appear.

•	Query processing
It refers to the algorithm or sequence of steps that is used to process a user’s query and retrieve the most relevant results.
The steps in query processing:
1.	Query understanding: Tokenisation of the query, linguistic analysis, and intent recognition. It considers user’s location and search history.
2.	Query rewriting and expansion: correcting spelling mistakes, normalizing terms.
3.	Information retrieval: searching against the database to find relevant results and ranking them based on relevance, quality and authority.
4.	Post processing and results display: Frontend to display the aggregated information.
•	Ranking
It refers to the website’s position in organic search results for a specific query. The ranking of the website mainly depends on the keyword matching, quality, quantity and backlinks, SEO, UX.
•	Difference between retrieval vs ranking
Ranking is basically making the website ordering based on various features and making it easy for the retrieval to happen, retrieval is basically querying the huge database of indexed websites and find the most relevant website, (ranking helps in achieving accurate results.)
Task
•	Draw architecture diagram by hand
•	Write 1-page explanation in your own words
Deliverable:
•	docs/system_overview.md ->done
________________________________________
Day 2 — Vector Space Model + TF-IDF
Learn deeply
•	Term Frequency
It measures how frequently a specific word or term appears within a document, calculated as a raw count or the ratio of the term’s occurrences to the total words in that document.
TF(t,d) = Number of times t appears in a document/ total number of words in document d
•	Inverse Document Frequency
It is used to calculate the number of documents within a collection that contain a specific term.
IDF =  log(Total documents/ document frequency)
It calculates whether the word occurs in the document irrespective of its frequency.
•	Cosine similarity
It calculates the similarity between two non-zero vectors by calculating the cosine of the angle between them, ranging from -1 to 1.
Task
•	Take 3 small documents
•	Compute TF-IDF manually on paper
•	Compute cosine similarity manually
Deliverable:
•	docs/tfidf_hand_calculation.md
If you can’t do this, stop and redo.
DONE!
________________________________________
Day 3 — Precision / Recall / MRR
Learn
•	Precision@k
It is a ranking metric which is used to evaluate the information retrieval and recommendation systems by measuring the proportion of relevant results in the top K results.
Precision@K = #number of relevant items in top K elements/K
•	Recall
It is used to measure the number of relevant items in the top K fetched results out of all the relevant results, (not just in the top K results).
Recall@k = #number of relevant results in the top K/total number of relevant items in the database.
•	Mean Reciprocal Rank
It is a metric which is used to in information retrieval and  recommendation systems that ranks the first relevant items.
It basically is used when we know what the result should be. We use different queries and note the rank of the most relevant item. 
MRR = 1/Q QSIGMAi=1 1/ranki
It is used in navigation, where the user only needs one, the best or the top result.
Task
•	Create 5 fake documents
•	Create 3 queries
•	Manually compute precision@3
Deliverable:
•	docs/evaluation_metrics.md
DONE!
________________________________________
WEEK 1 — Focused Crawler + Dataset Creation
Goal: Build your DSA corpus (200–500 docs)
________________________________________
Day 4 — Basic Scraper
Task:
•	Use requests + BeautifulSoup
•	Extract:
o	title
o	paragraph text
Test on 1 page.
Deliverable:
•	crawler/basic_scraper.py
pip install requests beautifulsoup4
created a basic scraper which first fetches the html from the given url, then parses html. After that it extracts the title using beautiful soup and them extracts content using ‘p’ tags in the document.
DONE.
________________________________________
Day 5 — BFS Crawler
Implement:
•	Queue
•	Visited set
•	Depth limit
•	Filter DSA-related links implemented using keywords, which can be expanded later on.
Concept focus:
Graph traversal in real system.
Okay, so I implemented a BFS crawler, wherein initially we start with a base url, and then we extract paragraphs from that page, and search for a tags, to search for more url, once obtain it, we crawl to that page, this is implemented using Bfs, so if we find a url in one page, we store that url in the queue, and keep searching for other urls in the same page, and keep storing it in the queue, once we exhaust the url’s in the page, we move on to the front of the queue, and move to that page.
DONE!!
