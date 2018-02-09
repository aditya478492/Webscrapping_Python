import requests
from bs4 import BeautifulSoup
import lxml

count=0.0
url = "https://www.yellowpages.ca/search/si/1/Coffee%20Shop/Windsor%2C%20ON";
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser");
each = soup.find_all("link")
for x in each:
    append=x.get("href")
    main="https://www.yellowpages.ca"+append
    try:
      c=requests.get(main)
      subsoup=BeautifulSoup(c.content,"html.parser");
      p=subsoup.find_all("span",{"itemprop":"streetAddress"});
      for d in p:
          print("Address : "+d.contents[0].strip())
      s = subsoup.find_all("span", {"class": "split-hours"})
      for x in s:
          print("Timings : "+x.contents[0].strip())
      name=subsoup.find_all("span",{"class":"merchant-title__name jsShowCTA"})
      for x1 in name:
        print("Name : "+x1.contents[0].strip()+"\n ")

    except:
        print("No information")







