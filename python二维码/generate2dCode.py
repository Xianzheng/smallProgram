import qrcode 
img = qrcode.make('http://fangxianzheng.natapp1.cc')

with open('test.png', 'wb') as f:
    img.save(f)