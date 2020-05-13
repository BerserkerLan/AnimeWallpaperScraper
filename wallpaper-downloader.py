from bs4 import BeautifulSoup
import requests
import urllib.request

i = 0
file1 = open("imageURLs.txt", "wt")
for page_num in range(1, 2000):
    page = requests.get("https://mobile.alphacoders.com/by-category/3?page=" + str(page_num))

    soup = BeautifulSoup(page.content, 'html.parser')
    soup.encode("utf-8")

    wallpaper_divs = soup.select('div a img', class_='item-element', href=True)
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    for div in wallpaper_divs:
        print(div)
        print("Page number" + str(page_num))
        # status_code = requests.get(div['src'].replace('thumb-', ''), headers=headers).status_code
        if (not('favicon' in div['src'])): 
            file1.write(str((div['src'].replace('thumb-', '') + " " + div['title']).encode('utf8')) + "\n")

file1.close()