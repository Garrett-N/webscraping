"""
grequests - requests in parallel
"""

import grequests

BATCH_LENGTH = 5

# An array with 25 urls
urls = ['https://google.com', 'https://yahoo.com', 'https://msn.com',
        'https://apple.com', 'https://microsoft.com', 'https://amazon.com', 'https://facebook.com']
# Our empty results array
results = []

while urls:
    # get our first batch of 5 URLs
    batch = urls[:BATCH_LENGTH]
    # create a set of unsent Requests
    rs = (grequests.get(url) for url in batch)
    # send them all at the same time
    batch_results = grequests.map(rs)
    # appending results to our main results array
    results += batch_results
    # removing fetched URLs from urls
    urls = urls[BATCH_LENGTH:]

print(results)