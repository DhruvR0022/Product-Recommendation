import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Set some default plot styles to make things look nice
# matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)
# plt.style.use('bmh')
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)


class FindBestItem:
    ans = ''

    def __init__(self, name_of_file, min_price, max_price):
        self.name_of_file = name_of_file
        self.min_price = min_price
        self.max_price = max_price
        self.data = pd.read_csv(self.name_of_file)
        self.filterData()
        self.typeConversion()
        self.dropDuplicates()

    # removing unwanted part of data/ polishing data
    def filterData(self):
        self.data['original_price'] = self.data['original_price'].str.replace(r',', '')
        self.data['discounted_price'] = self.data['discounted_price'].str.replace(r',', '')
        self.data['rating_number'] = self.data['rating_number'].str.replace(r',', '')

    # TYPE CONVERSION
    def typeConversion(self):
        self.data['original_price'] = pd.to_numeric(self.data['original_price'])
        self.data['discounted_price'] = pd.to_numeric(self.data['discounted_price'])
        self.data['rating'] = pd.to_numeric(self.data['rating'])
        self.data['rating_number'] = pd.to_numeric(self.data['rating_number'])

    def dropDuplicates(self):
        self.data = self.data.drop_duplicates(subset='name')

    # name itself tells it
    def filter_products_based_on_discounted_price(self):
        minimum_rating = 4  # self.data['rating'].mean()
        min_buyer_number = 10000    # self.data['rating_number'].mean()
        temp = self.data[
            ((self.data['discounted_price'] > self.min_price) & (self.data['discounted_price'] <= self.max_price))]
        temp = temp[((temp['rating'] > minimum_rating) & (temp['rating_number'] > min_buyer_number))].sort_values(
            'rating', ascending=False).head(10)
        self.ans = temp

    def writeAnswer(self):
        self.ans.to_csv('ans_of_' + self.name_of_file, index=False)

    def findBest(self):
        self.filter_products_based_on_discounted_price()
        self.writeAnswer()
