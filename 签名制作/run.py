import os
os.chdir('D:\developItem\demo_file\签名制作\赤壁子公司三分厂\赤壁子公司三分厂')
lst = []
for i in os.listdir():
    if i != '电子签名.py':
        lst.append(i)

# 
#os.chdir('D:\developItem\demo_file\签名制作\新建文件夹')
for i in lst:
    try:
        os.system('python 电子签名.py --image '+i)
    except:
        print(i,'出错')