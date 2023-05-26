import urllib.request


def getHtml(url):
    URL = url
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    request = urllib.request.Request(url=URL,headers = header)

    html = ''

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        
        if hasattr(e,'reason'):
            print(e.reason)

    return html

def write(url):
    html = getHtml(url)

    with open('record.txt','w',encoding='utf-8') as f:
        f.write(html)
