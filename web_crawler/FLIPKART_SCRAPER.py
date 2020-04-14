import requests  # required for HTTP requests: pip install requests
from bs4 import BeautifulSoup  # required for HTML and XML parsing
# from datetime import date
import time


class FlipkartScrapper:
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    search_item = ''

    def __init__(self, search_item):
        self.search_item = search_item

    # find desired class for link of item
    def findClass(self):
        r = requests.get('https://www.flipkart.com/search?q=' + self.search_item + '&page=1', headers=self.headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        class1 = '_2cLu-l'
        class2 = '_2mylT6'
        class3 = '_31qSD5'
        if bool(soup.find('a', attrs={'class': class1})):
            return class1
        else:
            if bool(soup.find('a', attrs={'class': class2})):
                return class2
            else:
                return class3

    # scrape all the links from website
    def flipkartLinkScrapper(self, page_start, page_end):
        temp_class = self.findClass()
        time.sleep(1)   # sleep to so website can't detact it
        links = []
        for i in range(page_start, page_end):
            # https://www.flipkart.com/search?q=Redmi&page=5
            r = requests.get('https://www.flipkart.com/search?q=' + self.search_item + '&page=' + str(i), headers=self.headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            temp = soup.findAll('a', attrs={'class': temp_class})
            links += temp
            print(str(i + 1) + ' no. page has ' + str(len(temp)) + ' links')
            time.sleep(0.1)

        links_set = set(links)
        return links_set

    def scrapeFlipkartProductInfo(self, link):
        data = []
        r = requests.get(link, headers=self.headers)  # ,proxies=proxies)
        soup = BeautifulSoup(r.content, 'html.parser')
        time.sleep(0.01)
        title = soup.find('span', attrs={'class': '_35KyD6'})
        rating = soup.find('div', attrs={'class': 'hGSR34'})
        rating_num = soup.find('span', attrs={'class': '_38sUEc'})
        original_price = soup.find('div', attrs={'class': '_3auQ3N _1POkHg'})
        discounted_price = soup.find('div', attrs={'class': '_1vC4OE _3qQ9m1'})

        if title is not None:
            data.append(title.text.strip().replace('\xa0', ' '))
        else:
            data.append('unknown')
        if original_price is not None:
            data.append(original_price.text.strip()[1:])
        else:
            data.append('-1')
        if discounted_price is not None:
            data.append(discounted_price.text.strip()[1:])
        else:
            data.append('-1')
        if rating is not None:
            data.append(rating.text.strip())
        else:
            data.append('-1')
        if rating_num is not None:
            r_n = rating_num.text.replace('\xa0', ' ')
            data.append(r_n[: r_n.find('Ratings')].strip())
        else:
            data.append('-1')

        data.append(link)
        return data
