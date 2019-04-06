
from bs4 import BeautifulSoup as bsoup
import argparse, urllib3, certifi, sys, json, os, shutil
import requests as rq
import csv 


import schedule
import time

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def scrape():
    '''Scrapes the craigslist web page at the given url.'''
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
    
    records = flatten(results)

    return records


def sqlDB():
    try:
        connection = mysql.connector.connect(host='localhost',database='python_db',user='user',password='password')

        records_to_insert = scrape()

        sql_insert_query = """ INSERT INTO python_users (title, price) VALUES (%s,%s) """

        cursor = connection.cursor(prepared=True)
        result = cursor.executemany(sql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "records inserted successfully")

    except mysql.connector.Error as error:
        print("Failed inserting record into python_users table {}".format(error))

    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("connection is closed")
        
# ''' Schedules the code to run at 3AM every day. '''
# schedule.every().day.at("03:00").do(scrape)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)


sqlDB()