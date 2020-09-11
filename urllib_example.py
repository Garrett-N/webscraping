"""
does what httpsocket.py does but using higher level library
we will also use lxml to do a little xpath parsing
"""

import urllib3
from lxml import html

# these three lines equal to httpsocket.py
http = urllib3.PoolManager()
r = http.request('GET', 'http://www.google.com')
print(r.data)

# play around with xpath parsing of links
data_string = r.data.decode('utf-8', errors='ignore')
tree = html.fromstring(data_string)
links = tree.xpath('//a')
for link in links:
    print(link.get('href'))