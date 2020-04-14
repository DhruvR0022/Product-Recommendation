# Product-Recommendation
A GUI app made in tkinter which crawl e-commerce site and find best product in user's budget.
# Prerequisite
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install  library
and tkinter from [here.](https://docs.python.org/3/library/tkinter.html)
```bash
pip install beautifulsoup4
```
```bash
pip install pandas
```
# Project Overview
  In this project we use **bs4** with the help of _requests_ to scrap data from website flipkart based of user input of given category
  and list out best product in avaliable category. User can also choose their budget.
  
 # Description
  First User will present with following UI where user can enter product, minimum price and maximum price.
  <br/>[])(images/image0.png)<br/>
  After clicking in search button it will open loading window while crawler scrape the site. it will take around few seconds for
  crawler to search enter product in website search bar and scrape from 48-80 different product based of amount page ans amount of number thread set in code 
  <br/>```image1```<br/>
  This Crawler can scrape as many as 700-800 products without any problem in few miniutes. Both no. of product and no. of threads(for multi-threading) are variable which are can be change by changing argument values to web crawler class.
  <br/>```image2```<br/>
  After Scraping all the data are saved in .csv file and with the help of * *pandas* * we find best product for user in given budget with best ratings and the amount of buyers. 
  <br/>```image3```<br/>
  In UI there is direct link given to each product page.
