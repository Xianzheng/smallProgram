
from bs4 import BeautifulSoup

def process():
    with open('record.txt','r',encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html,features='lxml')
        # result1 = soup.find_all('span',class_='privacy-type__grid-content privacy-type__data-category-heading')
        # for i in result1:
        #     print(i.text)
    string = ''
    result = soup.find_all(class_ = 'app-privacy__card')
    name = soup.find_all('h1', class_= 'product-header__title app-header__title')
    title = ''
    for i in name:

        title += i.text
    title = title.replace(' ','')
    title = title.replace('\n','')
    string += title+':'
    for i in result:
        # print(i.h3)
        tem = i.find_all('span',class_='privacy-type__grid-content privacy-type__data-category-heading')
        # print(i.h3.text)
        string +=  i.h3.text +':'
        for j in tem:
            # print(j.text)
            string += j.text
            string += '|'
        string += ';'
    string += '\n'
    print(string)
    with open('result.txt','a',encoding ='utf-8') as f:
        f.write(string)
        
        