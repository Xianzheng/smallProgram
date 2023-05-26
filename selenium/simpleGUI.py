
import PySimpleGUI as sg
'''
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
'''

print('gui test')


'''
#给gui按行布局
layout = [[sg.Text('Enter a Number')],      
          [sg.Input()],      
          [sg.OK()] ]

#生成gui
event, (number,) = sg.Window('Enter a number example').Layout(layout).Read()

#弹出框
sg.Popup(event, number)
'''


'''

sg.theme('Dark Grey 13')

layout = [[sg.Text('Filename')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Get filename example', layout)

event, values = window.read()
print(values)
window.close()

def ChatBot():
    layout = [[(sg.Text('This is where standard out is being routed', size=[40, 1]))],
              [sg.Output(size=(80, 20))],
              [sg.Multiline(size=(70, 5), enter_submits=True),
               sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
               sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

    window = sg.Window('Chat Window', layout, default_element_size=(30, 2))

    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
    while True:
        event, value = window.read()
        if event == 'SEND':
            print(value)
        else:
            break
    window.close()
ChatBot()





layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in  (None, 'Exit'):
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()


layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
          [sg.Cancel()]]

window = sg.Window('Custom Progress Meter', layout)
progress_bar = window['progressbar']
# loop that would normally do something useful
for i in range(1000):
    # check to see if the cancel button was clicked and exit loop if clicked
    event, values = window.read(timeout=10)
    if event == 'Cancel'  or event is None:
        break
  # update bar with loop value +1 so that bar eventually reaches the maximum
    progress_bar.UpdateBar(i + 1)
# done with loop... need to destroy the window as it's still open
window.close()
'''

from hashlib import sha1
import os,shutil

def gui():
    layout = [
            [sg.Text('你选择的文件夹是:',font=("宋体", 10)),sg.Text('',key='text1',size=(50,1),font=("宋体", 10))],
            [sg.Text('程序运行记录',justification='center')],
            [sg.Output(size=(70, 20),font=("宋体", 10))],              
            [sg.FolderBrowse('打开文件夹',key='folder',target='text1'),sg.Button('重命名'),sg.Button('关闭程序')]
            ]    
  
    window = sg.Window('雁陎的工具箱', layout,font=("宋体", 15),default_element_size=(50,1))  
  
    while True:
        event, values = window.read()
        if event in (None, '关闭'):   # 如果用户关闭窗口或点击`关闭`
            break
        if event == '重命名':
            if values['folder']:
                print('{0}正在重命名原文件为hash值{0}'.format('*'*10))
                mult_rename(values['folder'])
                print('{0}重命名完毕{0}'.format('*'*10))
            else:
                print('请先选择文件夹')
  
    window.close()


def calchash(file_path):  # 计算图片hash值
    with open(file_path,'rb') as f:
        sha1obj = sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash
 
  
def mult_rename(dir_path): # 批量重命名
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path,file)
        if not os.path.isdir(file_path): # 判断是否为文件夹         
            pic_hash = calchash(file_path)      # 计算hash值           
            last = file[file.rindex(r'.'):]  # 后缀
            new_name = pic_hash+last
            if file == new_name:
                print(file,'无需修改')
            else:
                try:
                    new_path = os.path.join(dir_path,new_name)
                    os.rename(file_path,new_path)
                    print('{0}已重命名为{1}'.format(file,new_name))
                except FileExistsError:
                    repeat_path = dir_path+r'\重复文件夹'
                    if os.path.exists(repeat_path) == False:
                        os.makedirs(repeat_path)
                    new_path = os.path.join(repeat_path,new_name)
                    shutil.move(file_path,new_path)
                    print(r'{0}文件重复，已移至重复文件夹下'.format(file))

def main():  
    gui()

if __name__ == '__main__':
    main() 