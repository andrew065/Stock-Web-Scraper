import json
import certifi
import pandas as pd
import requests
import urllib3
from bs4 import BeautifulSoup
from lxml import html
from openpyxl import load_workbook, Workbook


def get_request(url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    return http.request('GET', url)


def get_summary():
    url = "https://www.macrotrends.net/stocks/charts/AAPL/apple/financial-statements"
    request = requests.get(url)
    print(request.text)

    # summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
    # soup = BeautifulSoup(request, 'lxml')
    #
    # for x in summary_table:
    #     print(x.xpath('.//td[1]//text()'), x.xpath('.//td[2]//text()'))
