import requests, sys, webbrowser, bs4

print('Searching...')
res = requests.get('https://www.emag.ro/search/' + ''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')
linkElems = soup.select('div.card-item > div > div > div.card-section-mid > h2 > a')


#for link in linkElems:
#  newlink = link.get('href')

numOpen = min(5,len(linkElems))
for i in range(numOpen):
    urlToOpen = linkElems[i].get('href')
    print('Opening',urlToOpen)
    webbrowser.open(urlToOpen)
