import urllib
from urllib import error
from urllib import request
import sys
import re
import whois
from datetime import datetime
import time
from bs4 import BeautifulSoup, SoupStrainer

def getResponse(url):
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except urllib.error.URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        # everything is fine
        return(response)

def getHostname(url):
    hostname = url
    t = [(x.start(0), x.end(0)) for x in re.finditer('https://|http://|www.|https://www.|http://www.', hostname)]
    count = int(len(t))
    if count != 0:
        y = t[0][1]
        hostname = hostname[y:]
        t = [(x.start(0), x.end(0)) for x in re.finditer('/', hostname)]
        count = int(len(t))
        if count != 0:
            hostname = hostname[:t[0][0]]

    #print("Hostname is - " + hostname)
    return(hostname)

##1st feature
def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)'  # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        # print match.group()
        return 0
    else:
        # print 'No matching pattern found'
        return 1


#2nd feature
def url_length(url):
    if len(url) < 54:
        return 1
    elif len(url) >= 54 | len(url) <= 75:
        return 0
    else:
        return -1

#3rd feature
def shortening_service(url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net|safelinku\.net|bit\.ly|goo\.gl|tinyurl\.com|is\.gd|cli\.gs|pic\.gd|DwarfURL\.com'
                      '|ow\.ly|yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|tr\.im|twit\.ac'
                      '|su\.pr|twurl\.nl|snipurl\.com|BudURL\.com|short\.to|ping\.fm|Digg\.com|post\.ly|Just\.as'
                      '|\.tk|bkite\.com|snipr\.com|flic\.kr|loopt\.us|doiop\.com|twitthis\.com|htxt\.it|'
                      'AltURL\.com|RedirX\.com|DigBig\.com|short\.ie|u\.mavrev\.com|kl\.am|wp\.me'
                      '|u\.nu|rubyurl\.com|om\.ly|linkbee\.com|Yep\.it|posted\.at|xrl\.us|metamark\.net|sn\.im|hurl\.ws|eepurl\.com|idek\.net'
                      '|urlpire\.com|chilp\.it|moourl\.com|snurl\.com|xr\.com|lin\.cr|EasyURI\.com|zz\.gd|ur1\.ca'
                      '|URL\.ie|adjix\.com|twurl\.cc|s7y\.usshrinkify|EasyURL\.net|atu\.ca|sp2\.ro|Profile\.to|ub0\.cc|minurl\.fr|cort\.as'
                      '|fire\.to|2tu\.us|twiturl\.de|to\.ly|BurnURL\.com|nn\.nf|clck\.ru|notlong\.com|thrdl\.es|spedr\.com|vl\.am|miniurl\.com'
                      '|virl\.com|PiURL\.com|1url\.com|gri\.ms|tr\.my|Sharein\.com|urlzen\.com|fon\.gs|Shrinkify\.com|ri\.ms|b23\.ru|Fly2\.ws'
                      '|xrl\.in|Fhurl\.com|wipi\.es|korta\.nu|shortna\.me|fa\.b|WapURL\.co\.uk|urlcut\.com|6url\.com|abbrr\.com|SimURL\.com|klck\.me'
                      '|x\.se|2big\.at|url\.co\.uk|ewerl\.com|inreply\.to|TightURL\.com|a\.gg|tinytw\.it|zi\.pe|riz\.gd|hex\.io|fwd4\.me|bacn\.me|shrt\.st'
                      '|ln-s\.ru|tiny\.pl|o-x\.fr|StartURL\.com|jijr\.com|shorl\.com|icanhaz\.com|updating\.me|kissa\.be|hellotxt\.com|pnt\.me|nsfw\.in|xurl\.jp|yweb\.com'
                      '|urlkiss\.com|QLNK\.net|w3t\.org|lt\.tl|twirl\.at|zipmyurl\.com|urlot\.com|a\.nf|hurl\.me|URLHawk\.com|Tnij\.org|4url\.cc'
                      '|firsturl\.de|Hurl\.it|sturly\.com|shrinkster\.com|ln-s\.net|go2cut\.com|liip\.to|shw\.me|XeeURL\.com|liltext\.com|lnk\.gd|xzb\.cc'
                      '|linkbun\.ch|href\.in|urlbrief\.com|2ya\.com|safe\.mn|shrunkin\.com|bloat\.me|krunchd\.com|minilien\.com|ShortLinks\.co\.uk|qicute\.com'
                      '|rb6\.me|urlx\.ie|pd\.am|go2\.me|tinyarro\.ws|tinyvid\.io|lurl\.no|ru\.ly|lru\.jp|rickroll\.it|togoto\.us|ClickMeter\.com|hugeurl\.com'
                      '|tinyuri\.ca|shrten\.com|shorturl\.com|Quip-Art\.com|urlao\.com|a2a\.me|tcrn\.ch|goshrink\.com|DecentURL\.com|decenturl\.com|zi\.ma'
                      '|1link\.in|sharetabs\.com|shoturl\.us|fff\.to|hover\.com|lnk\.in|jmp2\.net|dy\.fi|urlcover\.com|2pl\.us|tweetburner\.com|u6e\.de'
                      '|xaddr\.com|gl\.am|dfl8\.me|go\.9nl\.com|gurl\.es|C-O\.IN|TraceURL\.com|liurl\.cn|MyURL\.in|urlenco\.de|ne1\.net|buk\.me|rsmonkey\.com|cuturl\.com|turo\.us'
                      '|sqrl\.it|iterasi\.net|tiny123\.com|EsyURL\.com|urlx\.org'
                      '|IsCool\.net|twitterpan\.com|GoWat\.ch|poprl\.com|njx\.me',str(url))
    if match:
        return -1
    else:
        return 1

def shortening_service_redirect(resp):
    #read html code
    html = resp.read()

    #use re.findall to get all the links
    links = re.findall('"((http|ftp)s?://.*?)"', str(html))
    links = [l[0] for l in links]
    for l in links:
        if shortening_service(l) == -1:
            #print(shortening_service(l))
            return 0
    return 1

def domain_registry_expiration(domain):
    expiration_date = domain.expiration_date
    # today = time.strftime('%Y-%m-%d')
    today = datetime.today()

    registration_length = 0
    # Some domains do not have expiration dates. The application should not raise an error if this is the case.
    if expiration_date:
        registration_length = abs((expiration_date - today).days)
    if registration_length / 365 <= 1:
        return -1
    else:
        return 1

def double_slash_redirecting(url):
    # since the position starts from, we have given 6 and not 7 which is according to the document
    list = [x.start(0) for x in re.finditer('//', url)]
    if list[len(list) - 1] > 6:
        return -1
    else:
        return 1

def prefix_suffix(domain):
    match = re.search('-', domain)
    if match:
        return -1
    else:
        return 1


def request_url(wiki, soup, domain):
    i = 0
    success = 0
    for img in soup.find_all('img', src=True):
        dots = [x.start(0) for x in re.finditer('\.', img['src'])]
        if wiki in img['src'] or domain in img['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for audio in soup.find_all('audio', src=True):
        dots = [x.start(0) for x in re.finditer('\.', audio['src'])]
        if wiki in audio['src'] or domain in audio['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for embed in soup.find_all('embed', src=True):
        dots = [x.start(0) for x in re.finditer('\.', embed['src'])]
        if wiki in embed['src'] or domain in embed['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for i_frame in soup.find_all('i_frame', src=True):
        dots = [x.start(0) for x in re.finditer('\.', i_frame['src'])]
        if wiki in i_frame['src'] or domain in i_frame['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    try:
        percentage = success / float(i) * 100
    except:
        return 1

    if percentage < 22.0:
        return 1
    elif 22.0 <= percentage < 61.0:
        return 0
    else:
        return -1

def main(url):

    status = []

    hostname = getHostname(url)
    response = getResponse(url)

    # with open('markup.txt', 'r') as file:
    #     soup_string = file.read()
    soup_string = response.read()
    soup = BeautifulSoup(soup_string, 'html.parser')

##1st feature added
    status.append(having_ip_address(url))
##2nd feature added
    status.append(url_length(url))
##3rd feature added
    status.append(shortening_service(url))
    # print(shortening_service_redirect(response))
##4th feature added
    status.append(shortening_service_redirect(response))

##5th feature  added
    dns = 1
    try:
        domain = whois.query(hostname)
    except:
        dns = -1

    if dns == -1:
        status.append(-1)
    else:
        status.append(domain_registry_expiration(whois.query(hostname)))

##6th feature added
    status.append(double_slash_redirecting(url))
##7th feature added
    status.append(request_url(url, soup, hostname))

    print(status)
    return(status)

#if __name__ == "__main__":
main(sys.argv[1])
