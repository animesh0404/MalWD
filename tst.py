import re
import sys
from urllib import request
from bs4 import BeautifulSoup, SoupStrainer


def main(url):
    # with open('markup.txt', 'r') as file:
    #     soup_string = file.read()
    opener = request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(url)
    # response = request.urlopen(url)
    soup_string = response.read()
    soup = BeautifulSoup(soup_string, 'html.parser')
    print(soup.prettify())

if __name__ == '__main__':
    main(sys.argv[1])
