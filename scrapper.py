#!/usr/bin/env python3

import urllib
from bs4 import BeautifulSoup
import webbrowser
from termcolor import colored, cprint

hackernews_url = "https://news.ycombinator.com/"
http_response = urllib.request.urlopen(hackernews_url)

f1 = open("hackernews_html", "w")
bytes = http_response.read()
content = bytes.decode('utf-8')
f1.write(content)
f1.close

open('hackernews', 'w').close()
f2 = open("hackernews", "w+")
f2.truncate()
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
    #print(row_data_element.find(text = True))
    #print(row_data_element_link.get("href"))
    f2.write(row_data_element.find(text = True))
    f2.write("\n")
    f2.write(row_data_element_link.get("href"))
    f2.write("\n")

f2.close()

f2 = open('hackernews', 'r')
text = f2.read()
lines = text.split("\n")

current_article = 1
webbrowser.open(lines[current_article], new = 1)
print("Opening "+ colored(lines[current_article - 1], 'green', attrs = ['bold']))

while current_article <= 57:
    next = input()

    if (next == "n"):
        current_article = current_article + 2
        webbrowser.open(lines[current_article], new = 1)
        print("opening " + colored(lines[current_article - 1], 'green'))

f2.close()
