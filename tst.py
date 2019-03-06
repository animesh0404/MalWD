import re

hostname = "https://www.google.com/index.html"

h = [(x.start(0), x.end(0)) for x in re.finditer('https://|http://|www.|https://www.|http://www.', hostname)]
z = int(len(h))
if z != 0:
    y = h[0][1]
    hostname = hostname[y:]
    h = [(x.start(0), x.end(0)) for x in re.finditer('/', hostname)]
    z = int(len(h))
    if z != 0:
        hostname = hostname[:h[0][0]]


print("Hostname is - " + hostname)
