import requests
from pages.quotes_page import QuotesPage

page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(page_content)

for quotes in page.quotes:
    print(quotes.content) #main file