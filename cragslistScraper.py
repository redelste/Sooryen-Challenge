
from bs4 import BeautifulSoup as bsoup
import argparse, urllib3, certifi, sys, json, os, shutil
import requests as rq
import csv 


base_url = "https://newyork.craigslist.org/search/sss?postal=07030"

r = rq.get(base_url)
soup = bsoup(r.content,'html5lib') # gets the HTML content of each page
totalCount = int(soup.findAll('span', attrs={'class':'totalcount'})[0].string)

results = []
for num in range(0, totalCount, 120):
    r = rq.get(base_url)
    soup = bsoup(r.content,'html5lib') # gets the HTML content of each page
    cur_url = base_url + "&s=" + str(num)
    resultInfo = soup.findAll('p',attrs={'class':'result-info'})
    results.append(list(map(lambda x: (x.select('.result-title')[0].string, x.select('.result-price')[0].string), resultInfo)))

flatten = lambda l: [item for sublist in l for item in sublist]

flat = flatten(results)
for x in range(len(flat)):
    print(x, flat[x])