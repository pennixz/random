from bs4 import BeautifulSoup
import urllib.request
import re
from random import randint

wikirandom = urllib.request.urlopen("https://wikipedia.org/wiki/Special:Random")
banned_links = ["Wikipedia:", "Category:", "Help:", "Special:", "Portal:", "Talk:", "Main_Page", "File:", "Template:"]


class Crawler:
    
    def __init__(self, trgt):
        self.target = trgt
        self.done = False
        self.soup = BeautifulSoup(wikirandom, 'html.parser')
        self.crawls = 0
        self.total = 0
        self.links = []
        self.interest = None
        print("Starting at ", self.soup.title.string)
        self.crawl()

    def crawl(self):
        
        while not self.done:
            
            for link in self.soup.findAll('a', attrs={'href': re.compile("^/wiki/")}):
                shrt = link.get('href')
                
                if (not any(word in shrt for word in banned_links)
                    and not any(wurd in shrt for wurd in self.links)):
                    self.links.append(link.get('href'))
                    self.total += 1
                    
                if self.target.lower() == shrt.strip('/wiki/').lower():
                    print("Jackpot! Found " + self.target + " in " + str(self.crawls) + " crawls!")
                    print("Looked at a total of " + str(self.total) + " URLs")
                    self.done = True
                    return
                
                if self.target.lower() in shrt.strip('/wiki/').lower():
                    self.interest = shrt
                else:
                    self.interest = None
                    
            if not self.interest:
                print("Nothing..")
                chosen_one = randint(0, len(self.links) - 1)
                page = urllib.request.urlopen("https://wikipedia.org" + self.links[chosen_one])
                self.soup = BeautifulSoup(page, 'html.parser')
                print("Crawling to " + self.links[chosen_one].strip('/wiki/'))
                self.links.pop(chosen_one)
                self.crawls += 1
            else:
                print("Found something related : " + self.interest.strip("/wiki/"))
                print("Crawling to it..")
                page = urllib.request.urlopen("https://wikipedia.org" + self.interest)
                self.soup = BeautifulSoup(page, 'html.parser')
                self.crawls += 1


print("input subject")
target = input()
crawly = Crawler(target)
