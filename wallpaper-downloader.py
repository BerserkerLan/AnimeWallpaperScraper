from bs4 import BeautifulSoup
import requests
import urllib.request
from git import Repo

PATH_OF_GIT_REPO = '.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

# file1 = open("imageURLs.txt", "wt")
# page = requests.get("https://mobile.alphacoders.com/by-category/3?page=1")
# soup = BeautifulSoup(page.content, 'html.parser')
# soup.encode("utf-8")
# pages = soup.select('input')[0]['placeholder'].replace('Page # / ','')

# max_page = int(pages)

# print(max_page)

# for page_num in range(1, max_page+1):
#     page = requests.get("https://mobile.alphacoders.com/by-category/3?page=" + str(page_num))

#     soup = BeautifulSoup(page.content, 'html.parser')
#     soup.encode("utf-8")

#     wallpaper_divs = soup.select('div a img', class_='item-element', href=True)
#     user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
#     headers={'User-Agent':user_agent,} 
#     for div in wallpaper_divs:
#         print(div)
#         print("Page number" + str(page_num))
#         # status_code = requests.get(div['src'].replace('thumb-', ''), headers=headers).status_code
#         if (not('favicon' in div['src'])): 
#             file1.write(str((div['src'].replace('thumb-', '') + " " + div['title']).encode('utf8')) + "\n")

# file1.close()
def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()