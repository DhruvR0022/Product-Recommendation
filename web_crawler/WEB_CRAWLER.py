from FLIPKART_SCRAPER import FlipkartScrapper
from threading import Thread
from queue import *
import time
import numpy as np


class WebCrawler:
    start_time = 0
    URL = ''
    objScrapper = ''
    objSaver = ''
    links = []
    list_of_links = []
    links_queue = Queue()
    thread_list = []
    thread_list_product = []
    data = []
    no_of_threads = 1

    def __init__(self, search_item, website, start_pages=0, end_pages=1, no_of_threads=1):
        self.search_item = search_item
        self.start_pages = start_pages
        self.end_pages = end_pages
        self.no_of_threads = no_of_threads
        self.website = website
        if self.website.upper() == 'FLIPKART':
            self.URL = 'https://www.flipkart.com'
            self.objScrapper = FlipkartScrapper(self.search_item)

    def startCounting(self):
        self.start_time = time.time()

    def endCounting(self):
        temp = self.start_time
        self.start_time = 0
        return int(time.time() - temp)

    # function use with multi-threading to returned save data
    def scrapeLinks(self, start, end):
        if self.website.upper() == 'FLIPKART':
            result = list(self.objScrapper.flipkartLinkScrapper(start, end))
        for r in result:
            self.links_queue.put(self.URL + r['href'])

    def getAllItemLinks(self):
        for i in np.arange(self.start_pages, self.end_pages, self.no_of_threads):
            # if last k pages are less than our counter
            if i + self.no_of_threads > self.end_pages:
                j = self.end_pages
            else:
                j = i + self.no_of_threads
            t = Thread(target=self.scrapeLinks, args=(i, j))
            t.start()
            self.thread_list.append(t)

        for th in self.thread_list:
            th.join()

        while not self.links_queue.empty():
            self.links.append(self.links_queue.get())
        print(len(self.links))

    def scrapMultipleItemInfo(self, idx):
        # idxx = idx[0]
        for datax in self.list_of_links[idx]:
            print(self.links.index(datax))
            temp_data = self.objScrapper.scrapeFlipkartProductInfo(datax)
            self.data.append(temp_data)

    def Cloning(self, li1):
        li_copy = []
        li_copy.extend(li1)
        return li_copy

    def sliceData(self):
        list_copy = self.Cloning(self.links)
        n = int(len(list_copy) / self.no_of_threads)
        print('n' + str(n))
        while True:
            temp_list = list_copy[0:n]
            self.list_of_links.append(temp_list)
            list_copy = list_copy[n:]
            if n > len(list_copy):
                temp_list += list_copy
                break

    def getAllItemInfo(self):
        self.sliceData()
        no_of_list = len(self.list_of_links)
        print(len(self.list_of_links))
        for idx in range(no_of_list):
            t = Thread(target=self.scrapMultipleItemInfo, args=([idx]))
            t.start()
            self.thread_list_product.append(t)

        for th in self.thread_list_product:
            th.join()

    def scrapIt(self):
        self.startCounting()
        self.getAllItemLinks()
        self.getAllItemInfo()
        x = self.endCounting()
        print('Total Excution time : ', end='\t')
        print(x, end='\t')
        print('seconds')
