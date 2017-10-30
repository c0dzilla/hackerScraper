#!/usr/bin/env python3

import os
import urllib
from bs4 import BeautifulSoup
import webbrowser
from termcolor import colored, cprint

hackernews_url = "https://news.ycombinator.com/"
http_response = urllib.request.urlopen(hackernews_url)

bytes = http_response.read()
content = bytes.decode('utf-8')

#file_src will store article titles and corresponding url
file_src = open('hackernews', 'w+')
soup = BeautifulSoup(content, "lxml")
table = soup.find('table', class_ = "itemlist")
table_rows = table.find_all("tr")

i = 0

for row in table_rows:
    i = i+1

    if i == 89:
        break

    if i%3 != 1 :
        continue
        
    row_data = row.find_all("td")
    row_data_element = row_data[2]
    row_data_element_link = row_data_element.find("a")
    file_src.write(row_data_element.find(text = True))
    file_src.write("\n")
    file_src.write(row_data_element_link.get("href"))
    file_src.write("\n")

file_src.close()

file_src = open('hackernews', 'r')
text = file_src.read()
lines = text.split("\n")
os.remove('hackernews')

current_article = 1
print(lines[current_article - 1])
while current_article <= 57:
    current_article = current_article + 2
    print(lines[current_article - 1])

current_article = 1
#webbrowser.open(lines[current_article], new = 1)
#print("Opening "+ colored(lines[current_article - 1], 'red', attrs = ['bold']))

while current_article <= 57:
    next = input()
    current_article = current_article + 2
    webbrowser.open(lines[current_article], new = 1)
    print("opening " + colored(lines[current_article - 1], 'red', attrs = ['bold']))