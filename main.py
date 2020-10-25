from bs4 import BeautifulSoup
import requests
import re

# Constants
URL = "https://www.reddit.com/r/bapcsalescanada/new/"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def main():
    page = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_ = 'scrollerItem', id = re.compile('^(t3_(.){6}$)'))

    # Extract data from each reddit post
    for result in results:
        post_title = result.find('h3').text
        post_timestamp = result.find('a', attrs = {'data-click-id': 'timestamp'})
        post_product_page = result.find('a', class_ = 'styled-outbound-link').attrs['href']
        post_reddit_page = post_timestamp.attrs['href']

        print("title: {}\ntimestamp: {}\nproduct page: {}\nreddit page: {}\n"
        .format(post_title, post_timestamp.text, post_product_page, post_reddit_page))

if __name__ == '__main__':
    main()
