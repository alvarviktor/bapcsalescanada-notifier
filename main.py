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

    for result in results:
        print(result.find('h3').text)

if __name__ == '__main__':
    main()