
from bs4 import BeautifulSoup

def process():
    with open('record.txt','r',encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html,features='lxml')
        result = soup.find_all(class_ = 'wGcURe')

        name = soup.find(class_ = 'Fd93Bb ynrBgc xwcR9d')
        string = ''
        try:
            string += name.text +' : '
        except:
            string += 'name not exist'
        for i in result:
            string += i.text + ' '
        with open('result.txt','a',encoding='utf-8') as f:
            f.write(string)
            f.write('\n')