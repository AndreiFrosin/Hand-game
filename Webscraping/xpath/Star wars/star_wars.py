import requests
from urllib.request import urlopen
from lxml import etree


#get html from site and write to local file
url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
headers = {'Content-Type': 'text/html'}
response = requests.get(url, headers = headers)
html = response.text

with open ('star_wars_html', 'w') as f:
    f.write(html)

#read local html file and set up lxml html parser
local = r'D:\Code\Webscraping\xpath\star_wars_html'
response = urlopen(local)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)

tree.xpath('//p[contains(text(),"Use")]/text()')
tree.xpath('//p/strong[not(contains(text(),"\xa0"))]/text()')
tree.xpath('//img[starts-with(@class, "alignnone")]/@src')
tree.xpath('//header[@class="article header"]/descendant::node()/text()')
tree.xpath('//li[@class="related-post"]/a/@href')
tree.xpath('//li[@class="related-post"]/a[1]/@href')
