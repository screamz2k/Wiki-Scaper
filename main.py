from bs4 import BeautifulSoup as BS
import requests as req
import threading
open("links.txt", "w").close()

def thread(link):
    new_links = scrape_links("https://en.wikipedia.org" + link)
    for lin in new_links:
        save_link(lin)

def save_link(link):
    if link.get("href") is not None:
        link = link.get("href")
    else:
        return
    if "/wiki/" in link and not "." in link and not ":" in link:
        cont = True
        with open("links.txt") as f:
            existing_links = f.read().splitlines()
            if link in existing_links:
                cont = False
        if cont:
            with open("links.txt", "a") as f:
                try:f.write(link + "\n")
                except:pass

def scrape_links(link):
    article = BS(req.get(link).content, "html.parser")
    return article.find_all("a")
links = scrape_links("https://en.wikipedia.org/wiki/" + input("https://en.wikipedia.org/wiki/"))
for link in links:
    save_link(link)
with open("links.txt") as f:
    for link in f.read().splitlines():
        threading.Thread(target=thread, kwargs={"link": link}).run()
