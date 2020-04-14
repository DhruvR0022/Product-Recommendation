from WEB_CRAWLER import *
from SAVE_DATA import *
from FIND_BEST_PRODUCT import *

class result:

    def __init__(self, title, min, max):
        self.title = title
        self.min = min
        self.max = max

    def getResult(self):
        self.website = 'flipkart'
        self.start_pages = 0
        self.end_pages = 1
        self.no_of_threads = 4
        self.webCrawlerObj = WebCrawler(self.title, self.website, self.start_pages, self.end_pages, self.no_of_threads)
        self.webCrawlerObj.scrapIt()
        self.data = self.webCrawlerObj.data
        print()
        print(len(self.data))
        self.saveDataObj = SaveData(self.data, self.title)
        self.saveDataObj.saveDataInCSVFile()
        self.dataFile = self.saveDataObj.name_of_file
        print(self.dataFile)
        self.pandasObj = FindBestItem(self.dataFile, self.min, self.max)
        print(len(self.pandasObj.data))
        self.pandasObj.findBest()
        self.ans_file = 'ans_of_' + self.pandasObj.name_of_file
        return self.ans_file


# testing
# obj = result('smartphone',999,39999)
# ans = obj.getResult()
# print(ans)
