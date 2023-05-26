from writeHtml import write
from analyze import process
import time
with open('ios.txt','r',encoding='utf-8') as f:
    urllst = f.readlines()

for url in urllst:
    print('work with',url)
    write(url)
    time.sleep(10)
    process()

# process()